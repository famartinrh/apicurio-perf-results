#!/bin/bash

REPORT_JAR=gatling-report.jar
if [[ ! -f $REPORT_JAR ]] ; then 
    wget --no-check-certificate https://maven-eu.nuxeo.org/nexus/service/local/repositories/vendor-releases/content/org/nuxeo/tools/gatling-report/6.0/gatling-report-6.0-capsule-fat.jar
    mv gatling-report-6.0-capsule-fat.jar $REPORT_JAR
fi

ALL_LOG_FILES=""
for logfile in $(find **/End2EndSimulation/*10u-600i/simulation.log) ; do
    ALL_LOG_FILES="$ALL_LOG_FILES $logfile"
done

CURRENT_REPORT=reports/$(date --iso-8601=seconds)

java -jar $REPORT_JAR $ALL_LOG_FILES -o $CURRENT_REPORT

java -jar $REPORT_JAR $ALL_LOG_FILES > $CURRENT_REPORT/stats.csv
