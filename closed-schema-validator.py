import os, sys


# Loop over each main topic
    # save all closed schemas into OK lists (subjects, oses, skill levels)....located in /learning-paths/<main_topic>/_index.md
    # Loop over each learning path in the main topic 
        # Grab the closed schema tag_type by name (subjects, oses, skill levels)......../learning-paths/<main_topic>/<learning-path>/_index.md
        # For each tag_type
            # Check if it is in the closed schema OK list
                # IF NOT, save path of file that was wrong, the tag_type that has an issue, and the specific tag that is not in the OK list

# Print OK if OK, or print all tags that were saved and wrong




# (file_path, tag_type, specific_tag)
not_ok_tags = []




def saveNextToOKList(file,OK_list):
    while(True):
        next_line = next(file).strip()
        if ( (next_line.startswith('-')) and (not '---' == next_line) ):
            OK_list.append(next_line.replace('-','').strip())
        else:
            return OK_list


def checkIfOK(current_line, file, learning_path_index_file, tag_type, OK_list, not_ok_tags):
    # check current line
    if ( (current_line.startswith('-')) and (not '---' == current_line) and (not tag_type in current_line) ):
        tag = line.replace('-:','').strip()
        if not tag in OK_list:
            not_ok_tags.append((learning_path_index_file, tag_type, tag ))      # (file_path, tag_type, specific_tag)

    while(True):
        next_line = next(file).strip()
        if ( (next_line.startswith('-')) and (not '---' == next_line) ):
            tag = line.replace('-:','').strip()
            if not tag in OK_list:
                not_ok_tags.append((learning_path_index_file, tag_type, tag ))      # (file_path, tag_type, specific_tag)
        else:
            return not_ok_tags



def showNotOKTags(not_ok_tag_list):
    if (len(not_ok_tag_list) == 0):
        print('All tags are OK!')
        sys.exit(0)
    else:
        print('Some tags found error. List:')
        for tag_tuple in not_ok_tag_list:
            print(tag_tuple[0])
            print('   '+tag_tuple[1])
            print('   '+tag_tuple[2])
            print()
        sys.exit(1)



python_file_path = os.path.dirname(os.path.realpath(__file__))

main_topic_dir = os.path.join(python_file_path,"content","learning-paths")

# Create empty closed schema lists
subjects_OK_list = []
operatingsystems_OK_list = []
skilllevels_OK_list = []

for subdir, main_topics, files in os.walk(main_topic_dir):
    # main_topics = ['cloud','desktop','embedded','microcontroller','mobile']
    for topic in main_topics:
        # Reset empty closed schema lists for this main topic
        subjects_OK_list = []
        operatingsystems_OK_list = []
        skilllevels_OK_list = ["Introductory","Advanced"]

        topic_index_file = os.path.join(main_topic_dir,topic,'_index.md')
        with open(topic_index_file, "r") as file:
            for line in file:
                if "subjects_closed_schema:" in line:
                    subjects_OK_list = saveNextToOKList(file,subjects_OK_list)
                if "oses_closed_schema:" in line:
                    operatingsystems_OK_list = saveNextToOKList(file,operatingsystems_OK_list)

        # Loop over each learning path in the main topic 
        for subdir, learning_paths, files in os.walk(os.path.join(main_topic_dir,topic)):
            for path in learning_paths:
                learning_path_index_file = os.path.join(main_topic_dir,topic,path,'_index.md')
                with open(learning_path_index_file, "r") as file:
                    for line in file:
                        if "skilllevels:" in line:
                            # easy to handle, same line
                            skill_level = line.replace('skilllevels:','').strip()
                            if not skill_level in skilllevels_OK_list:
                                not_ok_tags.append((learning_path_index_file, 'skilllevels', skill_level ))      # (file_path, tag_type, specific_tag)
                        elif "subjects:" in line:
                            not_ok_tags = checkIfOK(line,file, learning_path_index_file, 'subjects:', subjects_OK_list, not_ok_tags)
                        elif "operatingsystems:" in line:
                            not_ok_tags = checkIfOK(line,file, learning_path_index_file, 'operatingsystems:', operatingsystems_OK_list, not_ok_tags)

            break # can break after the first iteration, only need the first level of learning paths

    break # can break after the first iteration, only need the first level of main directories



showNotOKTags(not_ok_tags)


