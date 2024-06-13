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
From the input text, we are extracting the _id, title, tags, acceptance rate, and difficulty.
"""


def extract_leetcode_info(problem_string):
    """
    Extracts relevant information from a LeetCode problem string.

    Args:
        problem_string (str): The LeetCode problem string.

    Returns:
        dict: A dictionary containing the extracted information:
            - "_id" (str): The problem _id.
            - "title" (str): The problem title.
            - "tags" (list): A list of tags associated with the problem.
            - "acceptance_rate" (str): The acceptance rate of the problem.
            - "difficulty" (str): The difficulty level of the problem.
    """
    assert problem_string is not None, "Error in util: problem_string is None"
    # Split the input string into lines
    lines = problem_string.split("\n")

    # Extract _id and title from the first line
    _id_and_title = lines[0].split(".")
    assert (
        len(_id_and_title) == 2
    ), f"Error in util: _id and title not found \n_id_and_title:{_id_and_title}\nproblem_string:{problem_string}"
    _id = _id_and_title[0].strip()
    title = _id_and_title[1].strip()

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
        "_id": _id,
        "title": title,
        "tags": tags,
        "acceptance_rate": acceptance_rate,
        "difficulty": difficulty,
    }


def print_leetcode_info(infos):
    """
    Print out each of the extracted LeetCode information.
    """
    for info in infos:
        print("---------------------------")
        print(f"{info['_id']}. {info['title']}")
        print("tags: " + ",".join(info["tags"]))
        print("Acceptance Rate: " + info["acceptance_rate"])
        print("Difficulty: " + info["difficulty"])
        print("---------------------------")
