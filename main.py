import contextlib


def transform_to_combination_array(input: str) -> list[str]:
    if '"' in input:
        return []

    def separate_into_choice_lists(input: str):
        words = input.split(" ")
        choice_lists = []
        split_indices = []
        for i, word in enumerate(words):
            is_last_word = len(words) - i == 1
            if is_last_word:
                split_indices.append(i)
                continue
            with contextlib.suppress(IndexError):
                is_not_or = word != "OR"
                has_next_word = len(words) - i > 1
                next_word_is_not_or = words[i + 1] != "OR"
            if is_not_or and has_next_word and next_word_is_not_or:
                split_indices.append(i)
        index = 0
        for i in split_indices:
            temp = [word for word in words[index:i + 1] if word != "OR"]
            index = i + 1
            choice_lists.append(temp)
        return [x for x in choice_lists if x]

    def build_combinations(final_results: list[str], choice_lists: list[list[str]]):
        for choice_list in choice_lists:
            if len(final_results) == 0:
                final_results = choice_list
                continue

            temp = []
            for result in final_results:
                temp.extend(f'{result} {choice}' for choice in choice_list)
            final_results = temp
        return final_results

    final_results: list[str] = []
    choice_lists = separate_into_choice_lists(input)
    final_results = build_combinations(final_results, choice_lists)

    return final_results


if __name__ == "__main__":
    transform_to_combination_array("tt OR tischtennis OR tischtenis schläger OR schlaeger")
