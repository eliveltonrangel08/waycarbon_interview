setup_environment () {
  export PYTHONPATH='.'
  export $(grep -v '^#' ./.env | xargs)
}

options () {
  echo "Select an option: "
  echo "1 - setup the environment "
  echo "2 - migrate "
  echo "3 - upgrade "
  echo "0 - exit "

  read op

  case $op in
    0) exit 0;;
    1) setup_environment ;;
    2) migrate_command ;;
    3) upgrade_command ;;
  esac


}

migrate_command () {
  echo "Insert the migration message"
  read msg
  alembic revision --autogenerate -m "$msg"
}

upgrade_command () {
  alembic upgrade head
}

options