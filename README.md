Multiprocessing application to download and analyze a content of an html pages.

Every worker reads url from a kafka topic or stdin, runs it through a set of processors (called "stages") and
writes results to mongo or kafka output topic. Every stage has it's own config block. It looks like:

```python
[download_stage]  
connect_timeout = 3  
download_timeout = 3  
order = 10  
```

The only non-optional parameter is 'order'. It should be unique. Other parameters are optional and depends on a
particular stage. For instance, in case of 'download_stage', where we use python grab to download a page there are
two parameters:
    1. connect_timeout (maximum time to wait a server response)
    2. download_timeout (maximum time to download a page)
In this case we redefined those parameters.

All stages are split to different types (it is optional). It is possible to create your own stage, that does
something with the results from other stages. The basic workflow:
    1. Worker creates a Message object (empty container)
    2. It reads an input data (from kafka, stding or other)
    3. Message object goes through a set of stages (in a particular order)
    4. Every stage acqure some attribute from a Message object and does something with it.
       Then, a stage puts it's result (as an attribute) to a Message.
    5. If no exception occured, after the last stage is done, worker starts to work on a new input data.

Let's consider an example. There is a list of urls, which needs to be dowloaded and saved to a file. We wanna know, which
urls will be downloaded and which won't.
A set of stages will be the following:
    - stdin_reader_stage (to read urls one by one from a standard input)
    - download_stage (to download)
    - file_output_stage (to save results into file in a json format)

Additionally, we want to save results to two different files (downloaded, failed).
In such case we can use a single stage, but the configuration will look like:
```python
[STAGES]
stdin_reader_stage = 'classname':'StdinReaderStage'
download_stage = 'classname':'DownloadStage'
file_output_stage_failed = 'classname':'FileOutputStage','python_class_filename':'file_output_stage'
file_output_stage_downloaded = 'classname':'FileOutputStage','python_class_filename':'file_output_stage'
```

The usual format is the following:
<name_of_python_module> = 'classname':<name_of_python_class>

In the case of two different stages with the one pythone module config will be:
<custom_name_of_stage> = 'classname':<name_of_python_class>,'python_class_filename':<name_of_python_module>

Every stage has it's own configuration block:
```python
[stdin_reader_stage]
order = 0
owner = testing
comment = ''


[download_stage]
connect_timeout = 3
download_timeout = 3
order = 10

[file_output_stage_failed]
order = 20
out_dir = /tmp/shaman/data/failed
fields_to_print = results

[file_output_stage_downloaded]
order = 25
out_dir = /tmp/shaman/data/downloaded
fields_to_print = results
```

Running shaman on a small urls.txt file (it contains 2 urls):<br>
<b>cat urls.txt | python bin/daemon.py -i -c etc/crawler.config</b><br>
Output:<br>
<b>url : http://yandex.ru<br>
url : http://rambler.ru</b>

Results will be put in /tmp/shaman/data/downloaded/worker_[N], where N is a number of worker.

It is possible to create new stages and run them in any sequence desired. 
