import os

def sort_files_by_size():
    files_with_size = []
    for filename in os.listdir('.'):
        filepath = os.path.join('.', filename)
        if os.path.isfile(filepath):
            file_size = os.path.getsize(filepath)
            files_with_size.append((filename, file_size))

    sorted_files = sorted(files_with_size, key=lambda item: item[1], reverse=True)

    print("Файли у каталозі, відсортовані за розміром (від найбільшого до найменшого):")
    for filename, size in sorted_files:
        print(f"{filename}: {size} байт")

if __name__ == "__main__":
    sort_files_by_size()
