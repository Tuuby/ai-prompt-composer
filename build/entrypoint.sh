#!/usr/bin/env sh

# replace all occourences of "WEB_BASE_URL"
# with the value of the environment variable with the name
# "WEB_BASE_URL"
echo Value of environment variable WEB_BASE_URL: $WEB_BASE_URL
find '/usr/src/app/www' -name '*.js' -exec sed -i -e 's,WEB_BASE_URL,'"$WEB_BASE_URL"',g' {} \;

#run default start scirpt for python module
exec python3 -m AiPromptComposerApi