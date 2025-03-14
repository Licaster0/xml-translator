import os
import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import time

# Çeviri istatistiklerini tutacak bir sözlük
translation_stats = {
    "total_files": 0,
    "translated_files": 0,
    "total_words": 0,
    "translated_words": 0
}


def translate_text(text, translator, translation_dict=None):
    global translation_stats
    original_text = text
    # Çeviri sözlüğü kullanılıyorsa, metni sözlüğe göre çeviriyoruz
    if translation_dict:
        for term, translation in translation_dict.items():
            if term in text:
                text = text.replace(term, translation)

    # Çeviri işleminde kelime sayısını hesapla
    translation_stats["total_words"] += len(original_text.split())
    translated_text = translator.translate(text)
    translation_stats["translated_words"] += len(translated_text.split())

    return translated_text


def get_directory_path():
    while True:
        directory = input("Lütfen XML dosyalarının olduğu klasör yolunu girin: ").strip()
        if os.path.isdir(directory):
            return directory
        else:
            print("Geçersiz klasör yolu. Lütfen geçerli bir yol girin.")


def get_translation_dict():
    translation_dict = {}
    while True:
        add_terms = input("Çeviri sözlüğü eklemek ister misiniz? (Evet/Hayır): ").strip().lower()
        if add_terms == "evet":
            while True:
                term = input("Çevrilecek kelimeyi girin (Çıkmak için 'çık' yazın): ").strip()
                if term == "çık":
                    return translation_dict
                if not term:
                    print("Kelime boş olamaz. Lütfen geçerli bir kelime girin.")
                    continue
                translation = input(f"'{term}' için çeviri girin: ").strip()
                if not translation:
                    print("Çeviri boş olamaz. Lütfen geçerli bir çeviri girin.")
                    continue
                translation_dict[term] = translation
        elif add_terms == "hayır":
            return translation_dict
        else:
            print("Geçersiz yanıt. Lütfen 'Evet' veya 'Hayır' yazın.")


def translate_file(input_path, translator, translation_dict=None, pbar=None):
    global translation_stats
    try:
        tree = ET.parse(input_path)
        root = tree.getroot()

        for elem in root.iter():
            if elem.text and elem.text.strip():
                elem.text = translate_text(elem.text, translator, translation_dict)

            if elem.tail and elem.tail.strip():
                elem.tail = translate_text(elem.tail, translator, translation_dict)

        tree.write(input_path, encoding="utf-8")
        translation_stats["translated_files"] += 1

        if pbar:
            pbar.update(1)
        print(f"Çevrildi: {input_path}")
    except Exception as e:
        print(f"Hata oluştu: {input_path} - {e}")


def translate_xml_files_in_directory(directory, translation_dict=None, source_lang='en', target_lang='tr'):
    global translation_stats
    translator = GoogleTranslator(source=source_lang, target=target_lang)

    xml_files = [f for f in os.listdir(directory) if f.endswith(".xml")]
    if not xml_files:
        print("Bu klasörde çevirilecek XML dosyası bulunamadı.")
        return

    translation_stats["total_files"] = len(xml_files)

    # Çeviri işlemini paralel hale getirelim ve ilerleme çubuğunu doğru şekilde kullanalım
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        with tqdm(total=len(xml_files), desc="Çeviri işlemi", unit="dosya") as pbar:
            for filename in xml_files:
                input_path = os.path.join(directory, filename)
                futures.append(executor.submit(translate_file, input_path, translator, translation_dict, pbar))

            # İşlemlerin tamamlanmasını bekleyelim
            for future in futures:
                future.result()

    # Çeviri istatistiklerini yazdıralım
    print("\nÇeviri İstatistikleri:")
    print(f"Toplam dosya: {translation_stats['total_files']}")
    print(f"Çevrilen dosya: {translation_stats['translated_files']}")
    print(f"Toplam kelime: {translation_stats['total_words']}")
    print(f"Çevrilen kelime: {translation_stats['translated_words']}")


if __name__ == "__main__":
    source_lang = input("Kaynak dil kodunu girin (ör. en, tr, fr, vb.): ").strip()
    target_lang = input("Hedef dil kodunu girin (ör. en, tr, fr, vb.): ").strip()
    klasor_yolu = get_directory_path()
    translation_dict = get_translation_dict()

    start_time = time.time()  # Çeviri süresi başlangıcı
    translate_xml_files_in_directory(klasor_yolu, translation_dict, source_lang, target_lang)
    end_time = time.time()  # Çeviri süresi bitişi
    print(f"Çeviri işlemi tamamlandı. Toplam süre: {end_time - start_time:.2f} saniye.")
