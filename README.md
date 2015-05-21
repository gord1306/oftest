# oftest

To do OF 1.3 comformance test, we use the testcase from BII (http://www.biigroup.com/).

1. We use dpctl (https://github.com/CPqD/ofsoftswitch13) tool to send/recevie OF message.
   Because it doesn't print json format message, we have did modify code to ouput json format string,
   and modify some code for ease write test case.
2. We use python to run each test case.
3. 
