"""Prerequisites:
 - A database server (if you have no current one, then mysql will do fine)
 - The python driver for that database installed and working

In this bit of work, you will need perform the following steps:
 - Retrieve an archive
 - Extract the relevant data from the archive
 - Upload that data to your database server
 - Perform any steps necessary to prepare that data for querying
 - Generate queries about that data
 - Store the output of those queries in CSV format

The code presented here is incomplete. Every TODO entry has steps
involved that you will determine the best way to implement. You will
know that you have completed everything when running this script
completes successfully. When you have completed the exercise, zip up
the output files and your source code and return it to the email
supplied along with this test.

You may use any libraries you wish. The only restriction on this is
that Pulsepoint must be able to run your code, so the libraries must
be publicly available. If you do use any, please add them to the
REQUIRES string below.

You may rewrite as much of this source file as you wish. It is only
being provided as a possible skeleton, and is not required to have
this as the final form.

The COLUMN_DEFINITIONS provided below match the csv file that you will
download. In the original archive, there is also a file named
"codebook.txt" that provides definitions for each of these columns.

"""
import hashlib
import os
from datetime import datetime

REQUIRES = ""

# TODO: Update DBPARAMS here to set up the database connection
DBPARAMS = {
    }

COLUMN_DEFINITIONS = [
    ("ext1", "int"),
    ("ext2", "int"),
    ("ext3", "int"),
    ("ext4", "int"),
    ("ext5", "int"),
    ("ext6", "int"),
    ("ext7", "int"),
    ("ext8", "int"),
    ("ext9", "int"),
    ("ext10", "int"),
    ("est1", "int"),
    ("est2", "int"),
    ("est3", "int"),
    ("est4", "int"),
    ("est5", "int"),
    ("est6", "int"),
    ("est7", "int"),
    ("est8", "int"),
    ("est9", "int"),
    ("est10", "int"),
    ("agr1", "int"),
    ("agr2", "int"),
    ("agr3", "int"),
    ("agr4", "int"),
    ("agr5", "int"),
    ("agr6", "int"),
    ("agr7", "int"),
    ("agr8", "int"),
    ("agr9", "int"),
    ("agr10", "int"),
    ("csn1", "int"),
    ("csn2", "int"),
    ("csn3", "int"),
    ("csn4", "int"),
    ("csn5", "int"),
    ("csn6", "int"),
    ("csn7", "int"),
    ("csn8", "int"),
    ("csn9", "int"),
    ("csn10", "int"),
    ("opn1", "int"),
    ("opn2", "int"),
    ("opn3", "int"),
    ("opn4", "int"),
    ("opn5", "int"),
    ("opn6", "int"),
    ("opn7", "int"),
    ("opn8", "int"),
    ("opn9", "int"),
    ("opn10", "int"),
    ("ext1_e", "int"),
    ("ext2_e", "int"),
    ("ext3_e", "int"),
    ("ext4_e", "int"),
    ("ext5_e", "int"),
    ("ext6_e", "int"),
    ("ext7_e", "int"),
    ("ext8_e", "int"),
    ("ext9_e", "int"),
    ("ext10_e", "int"),
    ("est1_e", "int"),
    ("est2_e", "int"),
    ("est3_e", "int"),
    ("est4_e", "int"),
    ("est5_e", "int"),
    ("est6_e", "int"),
    ("est7_e", "int"),
    ("est8_e", "int"),
    ("est9_e", "int"),
    ("est10_e", "int"),
    ("agr1_e", "int"),
    ("agr2_e", "int"),
    ("agr3_e", "int"),
    ("agr4_e", "int"),
    ("agr5_e", "int"),
    ("agr6_e", "int"),
    ("agr7_e", "int"),
    ("agr8_e", "int"),
    ("agr9_e", "int"),
    ("agr10_e", "int"),
    ("csn1_e", "int"),
    ("csn2_e", "int"),
    ("csn3_e", "int"),
    ("csn4_e", "int"),
    ("csn5_e", "int"),
    ("csn6_e", "int"),
    ("csn7_e", "int"),
    ("csn8_e", "int"),
    ("csn9_e", "int"),
    ("csn10_e", "int"),
    ("opn1_e", "int"),
    ("opn2_e", "int"),
    ("opn3_e", "int"),
    ("opn4_e", "int"),
    ("opn5_e", "int"),
    ("opn6_e", "int"),
    ("opn7_e", "int"),
    ("opn8_e", "int"),
    ("opn9_e", "int"),
    ("opn10_e", "int"),
    ("dateload", "timestamp"),
    ("screenw", "int"),
    ("screenh", "int"),
    ("introelapse", "decimal(20,5)"),
    ("testelapse", "decimal(20,5)"),
    ("endelapse", "decimal(20,5)"),
    ("ipc", "int"),
    ("country", "char(2)"),
    ("lat_appx_lots_of_err", "decimal(9,6)"),
    ("long_appx_lots_of_err", "decimal(9,6)"),
]


def compare_results(resultfilename: str) -> bool:
    """Compares the contents of two files. The second file is always named
    f"{resultfilename}-correct". Returns True if they match, false if
    they do not.

    """
    return open(resultfilename).read() == \
        open(f"{resultfilename}-correct").read()


def shasum(filename: str) -> str:
    """Calculate the sha256 checksum of a file, and return that to the
    caller. Used to verify downloaded files and extracted files match
    what is expected to let the rest of the exercise work as desired.

    """
    digest = hashlib.sha256()
    with open(filename, 'rb') as reader:
        data = reader.read(65536)
        while data:
            digest.update(bytes(data))
            data = reader.read(65536)
    return digest.hexdigest()


def download_zip(url: str, zipfilename: str) -> None:
    """This function is expected to retrieve the zip file from the
    specified URL, and store that zip file in the current
    directory. It will fail if the output filename does not exist

    """
    # TODO: retrieve the file and save to disk in the current
    # directory. Note: This file is 160M

    assert os.path.exists(zipfilename)
    assert shasum(zipfilename) == \
        'd19ca933d974c371a48896c7dce61c005780953c21fe88bb9a95382d8ef22904'


def unpack_zip(zipfilename: str, datafilename: str) -> None:
    """This function is expected to extract a single file from the
    archive, and store that file in the current directory. It will
    fail if the file does not exist at the end.

    """
    # TODO: Extract the datafile and store it to disk in the current
    # directory. Note: The output file is nearly 400M

    assert os.path.exists(datafilename)
    assert shasum(datafilename) == \
        'dfbd5253f3f21f0569b34f2d1f47fbb71f5324ed26c3debbe29e84d42ce6d563'


def send_to_database(datafilename: str, dbname: str, tablename: str) -> None:
    """Take the data file, and store it as a table on the database
    server.

    """
    # TODO: send data to the database

    # TODO: any necessary preparations on the data after loading, and before
    # running the queries to come.


def total_record_count(dbname: str, tablename: str,
                       resultfilename: str) -> None:
    """
    Write out the count of records that exist in this table to resultfilename
    """
    # TODO: query for count of records, write to file
    assert os.path.exists(resultfilename)
    assert compare_results(resultfilename)


def times_by_country(dbname: str, tablename: str, resultfilename: str) -> None:
    """Write out the average total test time elapsed per country. This
    should include two columns: Country Code and
    average_number_seconds. It should be ordered alphabetically by
    country code

    """
    # TODO: Create the results file that shows the average time per country
    assert os.path.exists(resultfilename)
    assert compare_results(resultfilename)


def uniques_by_country(dbname: str, tablename: str,
                       resultfilename: str) -> None:
    """Write out the total number of unique visitors (IPC=1) per country
    that have at least 10,000 unique visitors. This list should be
    sorted so that the highest number of uniques is on top, and the
    lowest number of uniques is at the end. It should include two
    columns: country_code and count of unique visitors.

    """
    # TODO: create the results file for the unique visitors per country
    assert os.path.exists(resultfilename)
    assert compare_results(resultfilename)

def make_classes():
    """You will make three classes here inside of this function.
    
    1. Define a class called `Task`. This class needs to have a
    constructor that takes a datetime object and saves it as an
    instance member named `start_time`. It will also define an
    instance member named `results` and set it to `None`. This class
    also has a method named `run` which takes an arbitrary number of
    arguments as parameters. It should raise an exception when called.

    2. Define a class named `ListSum`. This class inherits from
    `Task`. The `run` method for this will take an arbitrary number of
    integers, and sum them up. It will store the sum in `results`.

    3. Define a class named `ListAverage`. This class inherits from
    `Task`. The `run` method will take an arbitrary number of
    integers, and average them. It will store the average in
    `results`.

    Add a method somewhere in this hierarchy that will allow you to
    compare two `Tasks` based on their `start_time`, so that we can
    list them in the order of their `start_time`.

    All the assert statements at the end of this function need to pass correctly.

    """

    t1 = Task(datetime.now())
    try:
        t1.run()
        raise Exception("You didn't generate an exception!")
    except Exception as e:
        if str(e) == "You didn't generate an exception!":
            raise e

    j1 = ListSum(datetime(2020, 1, 1, 0, 0, 0))
    j2 = ListAverage(datetime(2020, 6, 1, 0, 0, 0))
    jobs = [j2, j1]
    jobs.sort(key=lambda x: x.start_time)
    j1.run(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    j2.run(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    assert j1.results == 55
    assert j2.results == 5.5
    assert jobs == [j1, j2]

def main():
    """This is the method that is responsible for actually running the
    program. Feel free to modify it to suit your needs if the above
    skeleton does not meet what you wish it to.

    """
    url = "https://openpsychometrics.org/_rawdata/IPIP-FFM-data-8Nov2018.zip"
    zipfilename = "IPIP-FFM-data-8Nov2018.zip"
    datafilename = "data-final.csv"
    dbname = "ppdata"
    tablename = "big_five_research"
    countsfile = "counts.csv"
    country_times_file = "country_times.csv"
    country_uniques_file = "country_uniques.csv"

    download_zip(url, zipfilename)
    unpack_zip(zipfilename, datafilename)
    send_to_database(datafilename, dbname, tablename)
    total_record_count(dbname, tablename, countsfile)
    times_by_country(dbname, tablename, country_times_file)
    uniques_by_country(dbname, tablename, country_uniques_file)

    make_classes()


if __name__ == '__main__':
    main()
