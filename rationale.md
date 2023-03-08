This document shows the steps followed in the tool code to process the PDFs and fulfill the expected functions.

1. Input: Folder with PDF files

2. Extraction: Extract the PDF files from the folder

3. Processing: Process the PDF files with Grobid to convert them to XML

4. Transformation: Transform the XML to text

5. Extraction: Extract the abstract from the text

    5.1 Clean up the stopwords in the abstracts so as not to insert in the word cloud those that are not relevant to the meaning

6. Generation: Generate a keyword list from the abstract

7. Output: Display the generated image

8. Extraction: Extract the URLs of the PDFs from the text

    8.1 Clean up generic URLs such as https://doi.org

9. Output: Display the URLs of the PDFs on the screen

10. Extraction: Extract the number of images from the text

11. Generation: Generate a chart with the number of images for each file

12. Output: Display the generated graphic
