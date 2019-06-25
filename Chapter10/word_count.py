# 多使用几个文件
def count_words(filename):
    """计算一个文件有多少单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does't exist."
        # print(msg)
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(
            "The file " + filename + " has about " + str(num_words) + " words.")

# filename = 'alice.txt'
# count_words(filename)
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

# 失败时一声不吭 pass关键字