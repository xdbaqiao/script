#!/bin/bash
# This script is used to backup the svn data incrimentally.
#


now_time=`date +"%F %R"`


# parameters checking
if [ $# -ne 1 -a $# -ne 2 ]
then
    echo "      Error: The number of parameters error!"
    echo "      Usage: sh $0 <repository directory> [backup dir(optional)]"
    echo "      For example: sh $0 /home/svn/TEST /home/svn/TEST_backup.file"
    echo "                or sh $0 /home/svn/TEST"
    exit 1
fi


# which repository needs to backup
repository_dir=$1
if [ ! -d $repository_dir ]
then
    echo "$now_time  Error: Repository directory doesn't exist!"
    exit 1
fi


# the current version
current_version=`/usr/local/subversion/bin/svnlook youngest $repository_dir`
# backup directory
if [ $# -eq 2 ]
then
    backup_dir=$2
else
    backup_dir="${repository_dir}svn_repository_backup.file"
fi
# the previous version
if [ ! -f $backup_dir ]
then
    previous_version=0
else
    # find the last version in the backup_dir
    previous_version=`cat $backup_dir|awk  'BEGIN{x=0} /Revision-number:/{x++;a[x]=$NF} END{print a[x]}'`
    echo $previous_version |grep '^[0-9]*$' > /dev/null
    if [ $? -ne 0 ] || [ ! $previous_version ]
    then
        echo "$now_time  Error: the previous version is not number!"
        exit 1
    fi
fi


# if the version is different
if [ $previous_version -ne $current_version ]
then
    previous_version=$(($previous_version + 1))
    echo "$now_time  Begin incremental backup: From version $previous_version to $current_version, add to file $backup_dir..."
    /usr/local/subversion/bin/svnadmin dump --incremental --revision $previous_version:$current_version $repository_dir >> $backup_dir 
    echo "$now_time  Have done successfully!"
else
    echo "$now_time  Version is unchanged...no need for backup!"
fi


exit 0
