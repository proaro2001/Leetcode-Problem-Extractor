"""
This file is created to process the data.
The output looks like this:
---------------------------
50. Pow(x, n)
Math
Recursion
35.0%
Medium
---------------------------
From the input text, we are extracting the number, title, tags, acceptance rate, and difficulty.
"""


def extract_leetcode_info(problem_string):
    """
    Extracts relevant information from a LeetCode problem string.

    Args:
        problem_string (str): The LeetCode problem string.

    Returns:
        dict: A dictionary containing the extracted information:
            - "number" (str): The problem number.
            - "title" (str): The problem title.
            - "tags" (list): A list of tags associated with the problem.
            - "acceptance_rate" (str): The acceptance rate of the problem.
            - "difficulty" (str): The difficulty level of the problem.
    """
    # Split the input string into lines
    lines = problem_string.split("\n")

    # Extract number and title from the first line
    number_and_title = lines[0].split(".")
    number = number_and_title[0].strip()
    title = number_and_title[1].strip()

    # Extract tags from the following lines until acceptance rate
    tags = []
    for line in lines[1:]:
        if "%" in line:
            # When a percentage is encountered, assume it is the acceptance rate line
            acceptance_rate = line.strip()
            break
        else:
            tags.append(line.strip())

    # Extract difficulty from the last line
    difficulty = lines[-1].strip()

    return {
        "number": number,
        "title": title,
        "tags": tags,
        "acceptance_rate": acceptance_rate,
        "difficulty": difficulty,
    }


def print_leetcode_info(info):
    """
    Prints the extracted LeetCode problem information in a formatted way.

    Args:
        info (dict): A dictionary containing the extracted information.
    """
    print("---------------------------")
    print(f"{info['number']}. {info['title']}")
    print("tags: " + ",".join(info["tags"]))
    print("Acceptance Rate: " + info["acceptance_rate"])
    print("Difficulty: " + info["difficulty"])
    print("---------------------------")


# # Test the functions
# input = "50. Pow(x, n)\nMath\nRecursion\n35.0%\nMedium"
# info = extract_leetcode_info(input)
# print_leetcode_info(info)
