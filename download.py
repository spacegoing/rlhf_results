import wandb
import os
import re

# Initialize WandB API
api = wandb.Api()

# na
project_path = "t2njj6wv" # imgrew na_good
step_list = list(range(328,332))
media_dir = "na_good"
project_path = "s8c49d6j" # imgrew+
step_list = list(range(7))
media_dir = "na_bad"
project_path = "s8c49d6j" # imgrew+
step_list = list(range(390,393))
media_dir = "rew_good"
# color
project_path = "q2r231si" # imgrew+
step_list = list(range(5))
media_dir = "co_bad"
# step_list = list(range(390,393))
# media_dir = "co_good"


# Access the run
project_path = "yimfang/ddpo-pytorch/runs/" + project_path # na_good
run = api.run(project_path)

#*
# Directory to save the media files
os.makedirs(media_dir, exist_ok=True)


# Get all files for the specified step
files = run.files()

for file in files:
  match = re.search(r'images_(\d+)_',file.name)
  if match:
    step = int(match.group(1))
    if step in step_list:
      # Download and save the file
      file.download(root=media_dir, replace=True)
      print(f"Downloaded {file.name} from step {step}")

print("All media files downloaded.")
