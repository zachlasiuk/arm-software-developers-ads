---
# User change
title: "2b) Contribute: Metadata"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

This step will cover how to fill out Learning Path metadata over the three default files:
1. Metadata and Tagging - **_index.md**
2. Review Questions - **_review.md**
3. Next Steps - **_next-steps.md**

# Metadata and Tagging - _index.md

The following metadata is defined in the _index.md file:

| Learning Path Metadata | Explination |
|---------------|----------|
| title                 | Should start with a verb (learn, build, etc.), have no adjectives (amazing, cool, etc.), and be as concise as possible (limit one sentance).       |
| description           | One sentance summary of the learning path. |
| minutes_to_complete   | Time to reproduce a learning path from beginning to end (not just read it). |
| who_is_this_for       | One sentence indicating the exact target audience (developers in X industries using Y tools/software to accomplish Z). |
| learning_objectives   | 2-5 bullet points, one sentence each, describing what a reader will learn. Should start with a verb (Deploy, Measure). |
| prerequisites         | Details anything needed before this learning path can be started. Can include online service accounts, prior knowledge, previous Learning Paths, or specific tools and software. Offers explanitory links where possible. |

{{% notice Note%}}
To specify a prerequisite Learning Path, do so with a relative path like so:
* *The Learning Path on [Getting Started with Docker](../../docker) should be completed first.*
{{% /notice %}}

## Tags
Tagging metadata is also expected to increase findability via filtering. Some tags are closed (select from a pre-defined list), some are open (enter anything). The tags are:

### skilllevels (closed)
Indicates the skill level needed as a developer to complete this Learning Path.

| Option | Explination |
|--------------|--------------------|
| Introductory | requires minimal experience in this field or previous knowledge about the tools/software involved |
| Advanced     | requires experience with specific topics, tools, or software to properly understand this tutorial |

### subjects (closed)
Specifies the primary subject the learning path covers. Can only be one subject per learning path; if it spans multiple, pick the primary one. Select from the allowed list for each category, as defined here:

| Server and Cloud | Desktop and Laptop | Embedded | Mobile | Microcontroller |
|---------|---------|---------|---------|---------|
| ML | Windows on Arm| ML | ML | ML |
| CI-CD | Porting | CI-CD| CI-CD | CI-CD |
| Performance and Architecture | Performance and Architecture | Performance and Architecture | Performance and Architecture | Performance and Architecture |
| Containers and Virtualization | | Automotive | Gaming | Security |
| Databases | | Cloud Connection | Graphics | Cloud Connection  |
| Networking | | AR-VR | | Virtual Hardware |
| Storage | | Storage | | |
| Web | | Embedded Linux | | |
| Libraries | | | | |


### operatingsystems (closed)
Specifies the OS (or OSes) this learning path can run on. Select from this closed list:

| OS Options    |
|---------------|
| Linux         |
| Windows       |
| MacOS         |
| Android       |
| RTOS          |
| Baremetal     |


### arm_ips (open)
Specifies the Arm IP this learning path involves, providing a quick link to IP information for developers interested in learning more. You can enter multiple specifi c or groups of IP. More information:

| Grouping Type | When to use | Examples |
|--------------|-----|-----|
| Specific IP | when a tutorial covers a specific board or similar with one (or a few) Arm IP | Cortex-M4, Neoverse-N1, Mali-G57 |
| Group of IP | when a tutorial can be run across multiple Arm IP | Cortex-M, Cortex-A, Cortex-R, Neoverse, Mali |

### tools (open)
Specifies the tools this learning path leverages (or is about). Some examples below:

| Tool Type     | Examples |
|---------------|----------|
| Environments  | AWS EC2, GCP                      |
| Toolchains    | GCC, Arm Compiler for Embedded    |
| IDEs          | Arm Development Studio, VS Code   |
| Online Tools  | GitHub, Jenkins                   |
| Anything else | cbuild, Docker                    |

### softwares (open)
Specifies the software and software stacks this learning path leverages (or is about). Some examples below:

| Software Type | Examples |
|---------------|----------|
| Stack         | tinyML, CMSIS             |
| Language      | Python, Java, Assembly    |
| Libraries     | ????????????????????????  |


# Review Questions - _review.md

Review questions both validate path comprehension and re-enforce specific learning ideas. At least two questions should be provided; three questions is most common. Each question is multiple choice. They are specified in the _review.md file as follows:

| Review Metadata | Explination |
|---------------|----------|
| question          | a one sentance question to the reader       |
| answers           | the multiple choice answers  |
| correct_answer    | integer indicating what answer is correct (1 for the first listed, etc.)  |
| explination       | a short, 1-2 sentance explination of why the question has that answer.  |

For a great simple example of this concept see the [MongoDB Learning Path review](../../../server-and-cloud/mongodb/_review).

{{% notice %}}
The explination is displayed whether or not the reader selects the correct answer, so avoid phrases like "Correct! *This* is because..." and opt for phrasing like "*this* is correct because..."
{{% /notice %}}

# Next Steps - _next-steps.md

This is where you can provide a specific next step for a reader, and provide further reading resources to dive deeper into topics you covered. The following metadata is defined in the _next-steps.md file:

| Next Steps Metadata   | Explination |
|-----------------------|-------------|
| next_step_guidance    | 1-3 sentence description of how the reader can generally keep learning about these topics, and a specific explanation of why the next step is being recommended.   |
| recommended_path      | Link to the next learning path being recommended (For example, this could be [Learn How to Use Docker](../../docker)) |
| further_reading       | Links to references related to information covered |
| resource > title      | The displayed title of the provided further_reading resource |
| resource > link       | The website link to the specific resource |
| resource > type       | Helps the reader understand what type of resource is being suggested.  Can be either: (1) Manuals for a tool / software (type: documentation). (2) Blog about related topics (type: blog). (3) General online references (type: website). |
