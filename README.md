Automated Multimodal Literature Review Paper Writing Model
Overview
This project is designed to construct an automated multimodal large language model for generating literature review papers. The model integrates the reasoning abilities of large language models (such as GPT-3.5) with multimodal data sources, including images, videos, and audio, to create a system that simulates human intelligence. The model tackles several challenges in practical applications, including the difficulty of data acquisition, incomplete evaluation methods, and the current limitation of most writing models to handle only single-modal data.

Key innovations in this work include:

Data Acquisition & Processing: Using Selenium and LlamaIndex technologies, we achieve an 80% success rate in downloading academic papers.
Automated Literature Review Writing: Combining MetaGPT and MINT technologies, the system can autonomously write a literature review while evaluating both the process and outcome.
Multimodal Input/Output: The system supports multimodal inputs and outputs, combining text, images, and videos for a comprehensive review paper.
Experimental results demonstrate that the average time for generating a complete paper is under 15 minutes, which alleviates the challenges of data acquisition and evaluation, providing a solid foundation for future research and applications.

Project Files
class_dic.py
A class for creating a dictionary to store generated paper content.

img_match.py
Used for image matching, extracting paper-related images, and associating them with the appropriate paragraphs for insertion.

main.py
The main program responsible for generating the paper.

spider_final_doi.py
A literature crawling function that retrieves papers based on specified keywords.

vedio.py
Used for video synthesis, generating an introductory video.

Features
Multimodal Integration: Combines large language models with image, video, and audio data.
Efficient Data Crawling: Successfully retrieves academic papers with a high download success rate.
Automatic Paper Generation: Automates the process of generating literature review papers.
Fast Processing Time: Generates a full review paper in under 15 minutes.
Installation
To install and run the project, ensure you have Python 3.8 or above installed, along with the following dependencies:

bash
复制代码
pip install -r requirements.txt
Usage
Data Crawling:
Run the spider_final_doi.py script to crawl literature based on specific keywords.

bash
复制代码
python spider_final_doi.py
Generate Paper:
Use the main.py script to generate the literature review paper.

bash
复制代码
python main.py
Image Matching:
The img_match.py script will match images to relevant sections of the paper.

bash
复制代码
python img_match.py
Video Synthesis:
Generate a short introductory video using vedio.py.

bash
复制代码
python vedio.py
Conclusion
This project demonstrates the potential of multimodal large language models for automating literature review paper writing. By addressing the challenges of data acquisition and model evaluation, it lays a solid foundation for future developments in the field.
