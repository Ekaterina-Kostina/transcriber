from csv_reader.csv_reader import read_csv_file, save_csv_file
from stress_finder.stress_finder import restore_stress_by_transcription
from arg_parser.stress_finder_parser import parse_args
from common.constants import COL_WORD, COL_ORTHOEPIC_TRANS, COL_STRESSED_WORD


def main():
    args = parse_args()

    input_path = args.input_csv
    output_path = args.output_file
    failed_path = args.failed_file
    
    data_frame = read_csv_file(input_path, ',')
    data_frame =(
        data_frame[[COL_WORD, COL_ORTHOEPIC_TRANS]]
                .dropna(subset=[COL_WORD, COL_ORTHOEPIC_TRANS])
                .drop_duplicates(subset=[COL_WORD], keep='first')
                .reset_index(drop=True)
    )

    data_frame[COL_STRESSED_WORD] = [
        restore_stress_by_transcription(str(word), str(trans))
        for word, trans in zip(
            data_frame[COL_WORD],
            data_frame[COL_ORTHOEPIC_TRANS]
        )
    ]

    failed = data_frame[data_frame[COL_STRESSED_WORD].isna()]
    print(f'\nНе удалось определить ударение у {len(failed)} слов:')
    print(failed[[COL_WORD, COL_ORTHOEPIC_TRANS]].head(20))
    if failed_path is not None:
        save_csv_file(failed, failed_path)

    data_frame = data_frame.dropna(subset=[COL_STRESSED_WORD]).reset_index(drop=True)
    print(f'Слов после удаления проблемных: {len(data_frame)}')

    save_csv_file(data_frame, output_path)

if __name__ == '__main__':
    main()