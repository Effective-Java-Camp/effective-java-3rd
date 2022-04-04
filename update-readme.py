max_item = 90
weekly_item = 6
item_word = "Item "
target = "\n\n<br>\n\n## 📙"
new_readme = ""

def newItems(current_items):
    result = "|"
    week = int(current_item / weekly_item) + 1
    result += str(week)
    for i in range(current_item + 1, current_item + weekly_item + 1):
        result += ("|" + item_word + str(i))
    result += "|"
    return result

with open('readme.md', 'r', encoding="UTF-8") as f:
    text = f.read()
    current_item = text.count(item_word)
    if current_item < 90:
        before_readme = text.split(target)
        new_readme += before_readme[0]
        new_readme += "\n"
        new_readme += newItems(current_item)
        new_readme += target
        new_readme += before_readme[1]

with open('readme.md', 'w', encoding="UTF-8") as f:
    f.write(new_readme)
