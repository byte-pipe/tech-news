---
title: 'GitHub - SakanaAI/AI-Scientist-v2: The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search · GitHub'
url: https://github.com/SakanaAI/AI-Scientist-v2
site_name: github
content_file: github-github-sakanaaiai-scientist-v2-the-ai-scientist-v2
fetched_at: '2026-03-27T11:20:05.613424'
original_url: https://github.com/SakanaAI/AI-Scientist-v2
author: SakanaAI
description: 'The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search - SakanaAI/AI-Scientist-v2'
---

SakanaAI

 

/

AI-Scientist-v2

Public

* NotificationsYou must be signed in to change notification settings
* Fork460
* Star2.6k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

58 Commits
58 Commits
ai_scientist
ai_scientist
 
 
docs
docs
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
bfts_config.yaml
bfts_config.yaml
 
 
launch_scientist_bfts.py
launch_scientist_bfts.py
 
 
requirements.txt
requirements.txt
 
 
View all files

## Repository files navigation

# The AI Scientist-v2: Workshop-Level AutomatedScientific Discovery via Agentic Tree Search

📚[Paper]|
 📝[Blog Post]|
 📂[ICLR2025 Workshop Experiment]

Fully autonomous scientific research systems are becoming increasingly capable, with AI playing a pivotal role in transforming how scientific discoveries are made.
We are excited to introduce The AI Scientist-v2, a generalized end-to-end agentic system that has generated the first workshop paper written entirely by AI and accepted through peer review.

This system autonomously generates hypotheses, runs experiments, analyzes data, and writes scientific manuscripts. Unlikeits predecessor (AI Scientist-v1), the AI Scientist-v2 removes reliance on human-authored templates, generalizes across Machine Learning (ML) domains, and employs a progressive agentic tree search, guided by an experiment manager agent.

Note:The AI Scientist-v2 doesn’t necessarily produce better papers than v1, especially when a strong starting template is available. v1 follows well-defined templates, leading to high success rates, while v2 takes a broader, more exploratory approach with lower success rates. v1 works best for tasks with clear objectives and a solid foundation, whereas v2 is designed for open-ended scientific exploration.

Caution!This codebase will execute Large Language Model (LLM)-written code. There are various risks and challenges associated with this autonomy, including the potential use of dangerous packages, uncontrolled web access, and the possibility of spawning unintended processes. Ensure that you run this within a controlled sandbox environment (e.g., a Docker container). Use at your own discretion.

## Table of Contents

1. Requirements* Installation
* Supported Models and API Keys
2. Generate Research Ideas
3. Run AI Scientist-v2 Paper Generation Experiments
4. Citing The AI Scientist-v2
5. Frequently Asked Questions
6. Acknowledgement

## Requirements

This code is designed to run on Linux with NVIDIA GPUs using CUDA and PyTorch.

### Installation

#
 Create a new conda environment

conda create -n ai_scientist python=3.11
conda activate ai_scientist

#
 Install PyTorch with CUDA support (adjust pytorch-cuda version for your setup)

conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia

#
 Install PDF and LaTeX tools

conda install anaconda::poppler
conda install conda-forge::chktex

#
 Install Python package requirements

pip install -r requirements.txt

Installation usually takes no more than one hour.

### Supported Models and API Keys

#### OpenAI Models

By default, the system uses theOPENAI_API_KEYenvironment variable for OpenAI models.

#### Gemini Models

By default, the system uses theGEMINI_API_KEYenvironment variable for Gemini models through OpenAI API.

#### Claude Models via AWS Bedrock

To use Claude models provided by Amazon Bedrock, install the necessary additional packages:

pip install anthropic[bedrock]

Next, configure validAWS Credentialsand the targetAWS Regionby setting the following environment variables:AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,AWS_REGION_NAME.

#### Semantic Scholar API (Literature Search)

Our code can optionally use a Semantic Scholar API Key (S2_API_KEY) for higher throughput during literature searchif you have one. This is used during both the ideation and paper writing stages. The system should work without it, though you might encounter rate limits or reduced novelty checking during ideation. If you experience issues with Semantic Scholar, you can skip the citation phase during paper generation.

#### Setting API Keys

Ensure you provide the necessary API keys as environment variables for the models you intend to use. For example:

export
 OPENAI_API_KEY=
"
YOUR_OPENAI_KEY_HERE
"

export
 S2_API_KEY=
"
YOUR_S2_KEY_HERE
"

#
 Set AWS credentials if using Bedrock

#
 export AWS_ACCESS_KEY_ID="YOUR_AWS_ACCESS_KEY_ID"

#
 export AWS_SECRET_ACCESS_KEY="YOUR_AWS_SECRET_KEY"

#
 export AWS_REGION_NAME="your-aws-region"

## Generate Research Ideas

Before running the full AI Scientist-v2 experiment pipeline, you first use theai_scientist/perform_ideation_temp_free.pyscript to generate potential research ideas. This script uses an LLM to brainstorm and refine ideas based on a high-level topic description you provide, interacting with tools like Semantic Scholar to check for novelty.

1. Prepare a Topic Description:Create a Markdown file (e.g.,my_research_topic.md) describing the research area or theme you want the AI to explore. This file should contain sections likeTitle,Keywords,TL;DR, andAbstractto define the scope of the research. Refer to the example fileai_scientist/ideas/i_cant_believe_its_not_better.mdfor the expected structure and content format. Place your file in a location accessible by the script (e.g., theai_scientist/ideas/directory).
2. Run the Ideation Script:Execute the script from the main project directory, pointing it to your topic description file and specifying the desired LLM.python ai_scientist/perform_ideation_temp_free.py \
 --workshop-file"ai_scientist/ideas/my_research_topic.md"\
 --model gpt-4o-2024-05-13 \
 --max-num-generations 20 \
 --num-reflections 5* --workshop-file: Path to your topic description Markdown file.
* --model: The LLM to use for generating ideas (ensure you have the corresponding API key set).
* --max-num-generations: How many distinct research ideas to attempt generating.
* --num-reflections: How many refinement steps the LLM should perform for each idea.
3. Output:The script will generate a JSON file named after your input Markdown file (e.g.,ai_scientist/ideas/my_research_topic.json). This file will contain a list of structured research ideas, including hypotheses, proposed experiments, and related work analysis.
4. Proceed to Experiments:Once you have the generated JSON file containing research ideas, you can proceed to the next section to run the experiments.

This ideation step guides the AI Scientist towards specific areas of interest and produces concrete research directions to be tested in the main experimental pipeline.

## Run AI Scientist-v2 Paper Generation Experiments

Using the JSON file generated in the previous ideation step, you can now launch the main AI Scientist-v2 pipeline. This involves running experiments via agentic tree search, analyzing results, and generating a paper draft.

Specify the models used for the write-up and review phases via command-line arguments.
The configuration for the best-first tree search (BFTS) is located inbfts_config.yaml. Adjust parameters in this file as needed.

Key tree search configuration parameters inbfts_config.yaml:

* agentconfig:Setnum_workers(number of parallel exploration paths) andsteps(maximum number of nodes to explore). For example, ifnum_workers=3andsteps=21, the tree search will explore up to 21 nodes, expanding 3 nodes concurrently at each step.num_seeds: Should generally be the same asnum_workersifnum_workersis less than 3. Otherwise, setnum_seedsto 3.Note: Other agent parameters likek_fold_validation,expose_prediction, anddata_previeware not used in the current version.
* Setnum_workers(number of parallel exploration paths) andsteps(maximum number of nodes to explore). For example, ifnum_workers=3andsteps=21, the tree search will explore up to 21 nodes, expanding 3 nodes concurrently at each step.
* num_seeds: Should generally be the same asnum_workersifnum_workersis less than 3. Otherwise, setnum_seedsto 3.
* Note: Other agent parameters likek_fold_validation,expose_prediction, anddata_previeware not used in the current version.
* searchconfig:max_debug_depth: The maximum number of times the agent will attempt to debug a failing node before abandoning that search path.debug_prob: The probability of attempting to debug a failing node.num_drafts: The number of initial root nodes (i.e., the number of independent trees to grow) during Stage 1.
* max_debug_depth: The maximum number of times the agent will attempt to debug a failing node before abandoning that search path.
* debug_prob: The probability of attempting to debug a failing node.
* num_drafts: The number of initial root nodes (i.e., the number of independent trees to grow) during Stage 1.

Example command to run AI-Scientist-v2 using a generated idea file (e.g.,my_research_topic.json). Please reviewbfts_config.yamlfor detailed tree search parameters (the default config includesclaude-3-5-sonnetfor experiments). Do not setload_codeif you do not want to initialize experimentation with a code snippet.

python launch_scientist_bfts.py \
 --load_ideas 
"
ai_scientist/ideas/my_research_topic.json
"
 \
 --load_code \
 --add_dataset_ref \
 --model_writeup o1-preview-2024-09-12 \
 --model_citation gpt-4o-2024-11-20 \
 --model_review gpt-4o-2024-11-20 \
 --model_agg_plots o3-mini-2025-01-31 \
 --num_cite_rounds 20

Once the initial experimental stage is complete, you will find a timestamped log folder inside theexperiments/directory. Navigate toexperiments/"timestamp_ideaname"/logs/0-run/within that folder to find the tree visualization fileunified_tree_viz.html.
After all experiment stages are complete, the writeup stage begins. The writeup stage typically takes about 20 to 30 minutes in total. Once it finishes, you should seetimestamp_ideaname.pdfin thetimestamp_ideanamefolder.
For this example run, all stages typically finish within several hours.

## Citing The AI Scientist-v2

If you useThe AI Scientist-v2in your research, please cite our work as follows:

@article
{
aiscientist_v2
,
 
title
=
{
The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search
}
,
 
author
=
{
Yamada, Yutaro and Lange, Robert Tjarko and Lu, Cong and Hu, Shengran and Lu, Chris and Foerster, Jakob and Clune, Jeff and Ha, David
}
,
 
journal
=
{
arXiv preprint arXiv:2504.08066
}
,
 
year
=
{
2025
}

}

## Frequently Asked Questions

Why wasn't a PDF or a review generated for my experiment?

The AI Scientist-v2 completes experiments with a success rate that depends on the chosen foundation model, and the complexity of the idea. Higher success rates are generally observed when using powerful models like Claude 3.5 Sonnet for the experimentation phase.

What is the estimated cost per experiment?

The ideation step cost depends on the LLM used and the number of generations/reflections, but is generally low (a few dollars). For the main experiment pipeline, using Claude 3.5 Sonnet for the experimentation phase typically costs around $15–$20 per run. The subsequent writing phase adds approximately $5 when using the default models specified in the example command. Using GPT-4o formodel_citationis recommended as it can help reduce writing costs.

How do I run The AI Scientist-v2 for different subject fields?

First, perform theGenerate Research Ideasstep. Create a new Markdown file describing your desired subject field or topic, following the structure of the exampleai_scientist/ideas/i_cant_believe_its_not_better.md. Run theperform_ideation_temp_free.pyscript with this file to generate a corresponding JSON idea file. Then, proceed to theRun AI Scientist-v2 Paper Generation Experimentsstep, using this JSON file with thelaunch_scientist_bfts.pyscript via the--load_ideasargument.

What should I do if I have problems accessing the Semantic Scholar API?

The Semantic Scholar API is used to assess the novelty of generated ideas and to gather citations during the paper write-up phase. If you don't have an API key, encounter rate limits, you may be able to skip these phases.

I encountered a "CUDA Out of Memory" error. What can I do?

This error typically occurs when the AI Scientist-v2 attempts to load or run a model that requires more GPU memory than available on your system. To resolve this, you can try updating your ideation prompt file (ai_scientist/ideas/my_research_topic.md) to suggest using smaller models for the experiments.

## Acknowledgement

The tree search component implemented within theai_scientistdirectory is built on top of theAIDEproject. We thank the AIDE developers for their valuable contributions and for making their work publicly available.

## Star History

## ⚖️ License & Responsible Use

This project is licensed underThe AI Scientist Source Code License(a derivative of the Responsible AI License).

Mandatory Disclosure:By using this code, you are legally bound to clearly and prominently disclose the use of AI in any resulting scientific manuscripts or papers.

We recommend the following attribution in your paper's Abstract or Methods section:

"This manuscript was autonomously generated usingThe AI Scientist."

## About

The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search

### Resources

 Readme

 

### License

 View license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

2.6k

 stars
 

### Watchers

34

 watching
 

### Forks

460

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python70.4%
* TeX18.2%
* BibTeX Style7.3%
* JavaScript3.1%
* HTML1.0%