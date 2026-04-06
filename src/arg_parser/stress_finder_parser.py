import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(
        description='Восстановление ударения в словах по их орфоэпической транскрипции',
        usage='python3 main.py path/to/input.csv path/to/output.csv [path/to/error.csv]'
    )

    parser.add_argument(
        'input_csv',
        type=Path,
        help='Путь до файла со словами и орфоэпической транскрипцией'
    )

    parser.add_argument(
        'output_file',
        type=Path,
        help='Путь до файла для сохранения результата'
    )
    
    parser.add_argument(
        'failed_file',
        type=Path,
        help='Путь до файла c результатами ошибок. Может быть пустым, если не нужно сохранять ошибки',
        default=None
    )

    args = parser.parse_args()

    if not args.input_csv.exists():
        parser.error(f'Файл не найден: {args.input_csv}')

    if not args.input_csv.is_file():
        parser.error(f'Это не файл: {args.input_csv}')

    return args