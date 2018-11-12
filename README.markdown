Forcepoint Data Engineer Technical Exam
=======================================================

Getting Started
---------------

1. Work on your solution to the problem below locally.

2. When you are satisfied with your results, email the Forcepoint recruiter (who originally sent you the exam) with a
   zipped copy of your solution directory structure. **Don't include any files generated 
   by your solution**. We should be able to run any scripts you submit to generate output.

Compose a Data ETL Script
-------------------------------------

Please use a standard installation of Python 2.7 with standrd libraries.
[Unix] command line in the format:

```
> python parse-daily-enron-file.py source/enron-event-history-20180202.csv
```

The Enron event history data in included (.csv, adapted from the widely-used publicly available data set)

The columns contain:

* **time** - time is Unix time (in milliseconds)
* **message identifier**
* **sender**
* **recipients** - pipe-separated list of email recipients
* **topic** - always empty
* **mode** - always "email"

Your script should perform the following on the raw files in the "source" folder:

1. Convert each CSV row into JSON format, where the original **recipients** string has been split into a list of individual recipients. For example:
   {
      "time": "987611330000",
      "message identifier": "<HQ0VLJ5RRP5VD4LK2JMEAZETIQUIV0FAB@zlsvr22>",
      "sender": "phillip love",
      "recipients": ["jeffrey gossett", "greg whiting"],
      "topic": "",
      "mode": "email"
   }

2. Enrich converted email records in the following way:

   * Add an attributes array to each record and populate it with the number of recipients on the event:
   {
      "mode": "email",
      ...
      attributes: [
         {
            "name": "number_of_recipients",
            "value": 2
         }
      ]
   }

   * Rename the "time" field to "timestamp_iso" and convert the observed timestamp
     in millis to a UTC timestamp that is ISO 8601 compliant

   * Add a "unique_id" field that is a unique identifier for the message (you can
     generate your own or derive it from the input "message identifier" field)

3. Add logic to your script that...

   * Saves a COMPRESSED copy of the original CSV with "processed-<date>" appended
      to the filename to a "archive" directory (see the archive directory for an
      example)

   * Sutputs individual JSON record files into the "processed" folder (i.e.
      a CSV with 10 rows should result in 10 individual JSON files in "processed")

4. (Optional) Basic analytic task: Compute basic summary stats. For each entity,
   compute number of messages sent and received and generate a new CSV that
   contains this information.

Assessment
----------

Your solution will be assessed based on:

* attention to detail
* completion of the tasks
* algorithm efficiency
* code readability
* adherence to common coding practices that best enable sharing, re-using, and
  extending the code.
