# Word Count with Hadoop Streaming in Google Colab

This project demonstrates how to use Hadoop Streaming in Google Colab to count words in a text file.

## Files Included:
- `mapper.py`: The mapper script for counting individual words.
- `reducer.py`: The reducer script for summing the word counts.
- `wordcount.txt`: The input text file containing the text to be processed.
- `wordcount_result.txt`: The output file containing the word count results.

## Steps to Run:
1. Install Java 8.
2. Install Hadoop.
3. Set the `JAVA_HOME` and `HADOOP_HOME` environment variables.
4. Run the `mapper.py` and `reducer.py` scripts using Hadoop Streaming.
5. View the results in `wordcount_result.txt`.

## Requirements:
- Java 8
- Hadoop 3.x
