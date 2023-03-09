def slice_story(story):
    sliced_story = []
    word = []
    for index, letter in enumerate(story):
        if letter != " ":
            word.append(letter)
            if len(story) - 1 == index:
                sliced_story.append(word)
            elif story[index + 1] == " ":
                sliced_story.append(word)
                sliced_story.append(" ")
                word = []
    return sliced_story

def make_all_lines(story, maximum_charactes_line):
    lines = []
    line = []    
    available_space_line = maximum_charactes_line
    for index, word in enumerate(story):
        if len(word) <= available_space_line: 
            if word == " " and len(line) == 0:
                continue
            line.extend(word)
            available_space_line -= len(word)
        if line == [" "] and available_space_line < len(story[index + 1]):
            available_space_line = maximum_characters_line
            continue
        if available_space_line == 0 or index == (len(story) - 1): 
                lines.append(line)
                available_space_line = maximum_characters_line
                line = []  
        elif available_space_line < len(story[index + 1]): 
            lines.append(line)
            available_space_line = maximum_characters_line
            line = []
    return lines

def separate_lines_per_page(lines, maximum_characters_line):
    pages = []
    page = []
    available_lines_in_page = maximum_lines_page
    for index, line in enumerate(lines):
        if available_lines_in_page > 0:
            page.append(line)
            available_lines_in_page -= 1
        if available_lines_in_page == 0 or len(lines) - 1 == index:
            pages.append(page)
            available_lines_in_page = maximum_characters_line
            page = []
    return pages

all_test_cases_results = []

while True:
    try:
        story_infos = input().strip().split(" ")
    except (EOFError):
        break
    if story_infos == ['']:
        break
    [number_of_words_story, maximum_lines_page, maximum_characters_line] = map(lambda x: int(x), story_infos)
    story = list(input("").strip())
    story = slice_story(story)
    all_lines = make_all_lines(story, maximum_characters_line)
    pages = separate_lines_per_page(all_lines, maximum_lines_page)
    all_test_cases_results.append(len(pages))

for test_result in all_test_cases_results:
    print(test_result)

