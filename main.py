def restore_jpeg(original_path, corrupted_path, output_path):
    with open(original_path, 'rb') as original_file:
        original_data = original_file.read()
    with open(corrupted_path, 'rb') as corrupted_file:
        corrupted_data = corrupted_file.read()
    restored_data = bytearray(corrupted_data)
    block_size = 1024
    missing_blocks = []
    for i in range(0, len(original_data), block_size):
        original_block = original_data[i:i + block_size]
        corrupted_block = corrupted_data[i:i + block_size]
        if original_block != corrupted_block:
            missing_blocks.append((i, i + block_size))
    for start, end in missing_blocks:
        restored_data[start:end] = original_data[start:end]
    with open(output_path, 'wb') as output_file:
        output_file.write(restored_data)
    print(f"Восстановленный файл сохранён в {output_path}")
restore_jpeg('restored_original.jpg', 'corrupted1.jpg', 'brandnew.jpg')


''' def compare_and_restore(original_path, corrupted_path, output_path):
    with open(original_path, 'rb') as original_file:
        original_data = original_file.read()
    with open(corrupted_path, 'rb') as corrupted_file:
        corrupted_data = corrupted_file.read()
    original_hex = original_data.hex()
    corrupted_hex = corrupted_data.hex()
    differences = []
    min_length = min(len(original_hex), len(corrupted_hex))
    for i in range(0, min_length, 2):
        original_byte = original_hex[i:i + 2]
        corrupted_byte = corrupted_hex[i:i + 2]
        if original_byte != corrupted_byte:
            differences.append((i // 2, original_byte, corrupted_byte))
    if len(original_hex) > len(corrupted_hex):
        for i in range(min_length, len(original_hex), 2):
            differences.append((i // 2, original_hex[i:i + 2], "XX"))
    elif len(corrupted_hex) > len(original_hex):
        for i in range(min_length, len(corrupted_hex), 2):
            differences.append((i // 2, "XX", corrupted_hex[i:i + 2]))
    if not differences:
        print("Файлы идентичны. Восстановление не требуется.")
        return
    else:
        print(f"Найдено {len(differences)} различий:")
        for offset, original, corrupted in differences:
            print(f"Смещение: {offset:08X} | Оригинал: {original} | Повреждённый: {corrupted}")
    restored_data = bytearray(corrupted_data)
    with open(output_path, 'wb') as output_file:
        output_file.write(restored_data)
    print(f"Восстановленный файл сохранён в {output_path}")
compare_and_restore('human 1.jpg', 'human corr.jpg', 'restored_human.jpg') '''
