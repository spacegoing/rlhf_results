import json
import os


def generate_file_list(directory, prefix):
  """
    Generates a list of file paths with a specified prefix for all jpg files in the given directory.
    """
  file_list = []
  for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
      file_list.append(prefix + filename)
  return file_list


# Define the base directory and prefix
base_directory = "/home/jddesk/jdDeskCodeLab/wandb_api"
prefix = 'https://raw.githubusercontent.com/spacegoing/rlhf_results/master/'

# NA
na_good_list = generate_file_list(
    os.path.join(base_directory, "na_good"), prefix + 'na_good/')
na_bad_list = generate_file_list(
    os.path.join(base_directory, "na_bad"), prefix + 'na_bad/')
rew_good_list = generate_file_list(
    os.path.join(base_directory, "rew_good"), prefix + 'rew_good/')

# Color
co_good_list = generate_file_list(
    os.path.join(base_directory, "co_good"), prefix + 'co_good/')
co_bad_list = generate_file_list(
    os.path.join(base_directory, "co_bad"), prefix + 'co_bad/')

#*
q_list = []

# for i, (good, bad) in enumerate(zip(na_good_list, na_bad_list)):
for i, (good, bad) in enumerate(zip(rew_good_list, na_bad_list)):
# for i, (good, bad) in enumerate(zip(co_good_list, co_bad_list)):
  q_list.append({
      "index":
          i,
      "prompt":
          "An animal is colored a weird color",
      "refImgs": [],
      "reverse":
          False,
      "img1":
          good,
      "img2":
          bad,
      "question": [{
          "issue": "Which image if of higher quality",
          "option": [
              "I prefer image A", "I am indifferent", "I prefer image B"
          ],
          "answer": -1
      }]
  })

with open('rlhf.json','w') as f:
# with open('color.json','w') as f:
# with open('rew.json','w') as f:
  json.dump(q_list, f)
