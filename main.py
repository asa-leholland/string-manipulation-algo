def transform_to_combination_array(input: str) -> list[str]:
    final_results: list[str] = []

    words = input.split(" ")
    lists_between_ors = []
    temp = []
    for word in words:
        if word == "OR":
            last_word = temp.pop()
            lists_between_ors.append(temp)
            temp = [last_word]
        else:
            temp.append(word)
    lists_between_ors.append(temp)

    for choice_list in lists_between_ors:

        if len(final_results) == 0:
            final_results = choice_list
            continue
        if len(choice_list) == 1:
            for result, i in enumerate(final_results):
                final_results[i] = f"{result} {choice_list[0]}"
            for result in final_results:
                result = final_results.append(choice_list[0])
            continue

        temp = []
        for choice in choice_list:
            temp.extend(f'{result} {choice}' for result in final_results)
        final_results = temp

    return final_results



if __name__ == "__main__":
    transform_to_combination_array("tischtennis schläger OR schlaeger")
