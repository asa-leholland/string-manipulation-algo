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
        print('final_results', final_results)
        print('choice_list', choice_list)

        if len(final_results) == 0:
            final_results = choice_list
            continue
        if len(choice_list) == 1:
            for result, i in enumerate(final_results):
                print('result', result)
                final_results[i] = result + " " + choice_list[0]
            for result in final_results:
                result = final_results.append(choice_list[0])
            continue

        choice_count = len(choice_list)
        temp = []
        for choice in choice_list:
            for result in final_results:
                temp.append(f'{result} {choice}')
        final_results = temp


    return final_results


if __name__ == "__main__":
    transform_to_combination_array("tischtennis schläger OR schlaeger")
