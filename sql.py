import os
command = "sqlcmd"
schema = "rsa_reports"
# reportsRdr, webReportDataGenerator
query_str = "SELECT count(*) as Event_count FROM [SCHEDULER_TASK_RUN_LOG] where JOB_NAME like '%reportsRdr%' and START_TIME >'2021-05-01 00:00:00.897' and START_TIME <'2021-05-31 00:00:00.897' and status in (0,2)"
delimiter = '|'
separator = str(''.join(['-s', "'", delimiter, "'"]))
tenants = open('tenants.txt',"r")

for tenant_name in tenants:
 tenant_name=tenant_name.strip('\n')
 db_name = str('_'.join([schema, tenant_name]))
 shell_cmd = str(' '.join(
  [command,
   '-S', '10.4.8.6', separator,
   '-U', 'sa',
   "-P", 'S@cur*A!!',
   '-d', db_name,
   '-Q', '\"', query_str, '\"']))
 query_output = os.popen(shell_cmd).read().split('\n')

 if len(query_output) > 1:
  del query_output[1]
  del query_output[-3:]
 output = []
 # Convert list to matrix
 for i in range(len(query_output)):
  output.append(query_output[i].split('|'))
 # Remove spaces from the end and beginning
 for i in range(len(output)):
  for y in range(len(output[i])):
   output[i][y] = output[i][y].strip()
 print(tenant_name, output[i])
tenants.close()

