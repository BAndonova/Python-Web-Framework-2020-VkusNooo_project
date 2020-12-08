# shellcheck disable=SC2164
# shellcheck disable=SC2162

cd
cd PycharmProjects/alienclouds
pip freeze > requirements.txt
#git config --global user.email "your mail"
git add .
echo "What did y🦠u change?"
read msg
git commit -m "$msg"
git push -u origin master