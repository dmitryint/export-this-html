#!/bin/bash

# Must udpate those two VARS
DEPLOY_ID=g10000124
URL_TO_PARSE=http://pascalandy.com/blog/landingpage_data_v2/
#
#
#
#
#
TEMPLATE_ID=THEME_ID_Identity
HTMLEXPORT_PROJECT_PATH=/Users/p_andy/Documents/_pascalandy/11_FirePress/GitLab/firepress-static_grp/22-all-in/_generator_identity
STATIC_CONTENT_PATH=/Users/p_andy/Documents/_pascalandy/11_FirePress/GitLab/firepress-static_grp/22-all-in/$DEPLOY_ID/static_content_env
GITLAB_LOCAL_REPO=/Users/p_andy/Documents/_pascalandy/11_FirePress/GitLab/firepress-static_grp/22-all-in
TEMPLATE_ID_PATH=$GITLAB_LOCAL_REPO/$TEMPLATE_ID
HTML_FINAL_OUTPUT=$GITLAB_LOCAL_REPO/$DEPLOY_ID
#
#
#
#
#


# Position the terminal
cd $HTMLEXPORT_PROJECT_PATH; \
pwd; ls -AlhF; du -sh; echo; \


# Copy template
rm -rf $HTML_FINAL_OUTPUT; \
mkdir $HTML_FINAL_OUTPUT; \
cp -R -v $TEMPLATE_ID_PATH/. $HTML_FINAL_OUTPUT/. ; \
rm $HTML_FINAL_OUTPUT/index.html; \
rm $HTML_FINAL_OUTPUT/README.md; \


# Get variables from url:
python3 run.py --url=$URL_TO_PARSE --out-file=$STATIC_CONTENT_PATH; \
cat $STATIC_CONTENT_PATH; \


# Generate html from template:
python3 generate_from_template.py \
	--template=$TEMPLATE_ID_PATH/index.html \
	--env=$STATIC_CONTENT_PATH >$HTML_FINAL_OUTPUT/index.html ;


# Preview the HTML file
sleep 1; \
cd "$HTML_FINAL_OUTPUT"; \
open -a "Google Chrome" index.html; \
sleep 1; \

# Git commit changes
git add -A; \
git commit -m "$DEPLOY_ID HTML export"; \
git push; sleep 2;