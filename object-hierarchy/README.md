# Constructing An Object Hierarchy

Using the programming language of your choice, construct a simplified
class hierarchy that could be used to implement the below
requirements. Note that you do not have to do *any*
implementations. For instance, empty methods, methods that have
missing parameters, these are all acceptable. We're really only
seeking the names of the classes, the inheritance you choose, and any
important methods you identify.

Remember: Don't actually implement this, since you can spend days
working on it to make it so you're happy with the results. Just show
us the simple class and method definitions (and parameters are
optional for them!)

Don't forget to include a call that starts the process to turn from
input config to output file.

# Requirements

We are creating a tool that transforms configuration files into jobs
that can be executed. These are simplified jobs, and will include
steps like "read this file", "run this query", etc. An example
configuration file is below, along with a sample output.

# Sample Configuration File

```
name: rpthourly
description: aggregate the data from the logevent stream into summary data
tasks:
  run_this_query:
    select
	  customerid,
	  campaignid,
	  sum(impressions),
	  sum(revenue),
	  sum(costs)
	from logevent
	where day=today()
	  and hour=now()
```

# Sample Output (located in rpthourly.py)

```
import airflow
from airflow.operators.python_operator import PythonOperator
description = """
The bhlogevent flow is used by the Exchange to monitor traffic.
"""

def run_this_query(*p, **kwargs):
    db.conn().cursor().execute(kwargs['query'])

with airflow.DAG(
    dag_id="rpthourly",
) as dag:
    task000 = PythonOperator(
        task_id='run_this_query',
        provide_context=True,
        python_callable=run_this_query,
        op_kwargs={
		    query: """
    select
	  customerid,
	  campaignid,
	  sum(impressions),
	  sum(revenue),
	  sum(costs)
	from logevent
	where day=today()
	  and hour=now()
"""
        }
    )
```
