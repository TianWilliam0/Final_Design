# Automated Multimodal Literature Review Paper Writing Model
## This code is for communication learning only, if you need reference, please indicate the source.
## Overview

This project is designed to construct an automated multimodal large language model for generating literature review papers. The model integrates the reasoning abilities of large language models (such as GPT-3.5) with multimodal data sources, including images, videos, and audio, to create a system that simulates human intelligence. The model tackles several challenges in practical applications, including the difficulty of data acquisition, incomplete evaluation methods, and the current limitation of most writing models to handle only single-modal data.

Key innovations in this work include:
- **Data Acquisition & Processing**: Using Selenium and LlamaIndex technologies, we achieve an 80% success rate in downloading academic papers.
- **Automated Literature Review Writing**: Combining MetaGPT and MINT technologies, the system can autonomously write a literature review while evaluating both the process and outcome.
- **Multimodal Input/Output**: The system supports multimodal inputs and outputs, combining text, images, and videos for a comprehensive review paper.

Experimental results demonstrate that the average time for generating a complete paper is under 15 minutes, which alleviates the challenges of data acquisition and evaluation, providing a solid foundation for future research and applications.

## Project Files

1. **`class_dic.py`**  
   A class for creating a dictionary to store generated paper content.

2. **`img_match.py`**  
   Used for image matching, extracting paper-related images, and associating them with the appropriate paragraphs for insertion.

3. **`main.py`**  
   The main program responsible for generating the paper.

4. **`spider_final_doi.py`**  
   A literature crawling function that retrieves papers based on specified keywords.

5. **`vedio.py`**  
   Used for video synthesis, generating an introductory video.

6. **`Presentation file.mp4`**  
   A demonstration video showing how the system works and its capabilities.

## Features

- **Multimodal Integration**: Combines large language models with image, video, and audio data.
- **Efficient Data Crawling**: Successfully retrieves academic papers with a high download success rate.
- **Automatic Paper Generation**: Automates the process of generating literature review papers.
- **Fast Processing Time**: Generates a full review paper in under 15 minutes.



