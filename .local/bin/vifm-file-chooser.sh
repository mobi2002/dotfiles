#!/usr/bin/env sh
TMP="/tmp/vifm-file-$$"
if [ "$1" = "-d" ]; then
	st -c "vifm-file-chooser"  -T "File Chooser" -e vifm --choose-dir $TMP -c only --on-choose " "
elif [ "$1" = "-f" ]; then
	st -c "vifm-file-chooser"  -T "File Chooser" -e vifm --choose-files $TMP -c only
else
	echo "Specify a valid option:\n-d for directory selection.\n-f for file selection."
	exit 1
fi

[ -f $TMP ] || exit 1
cat $TMP
rm $TMP
