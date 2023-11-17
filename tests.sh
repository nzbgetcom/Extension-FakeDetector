# python versions for running tests
PYTHON_VERSIONS="3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 3.10 3.11 3.12"
# python version that does not allow failed tests
SUPPORTED_PYTHON_VERSIONS="3.9 3.10 3.11 3.12"
# test script name
TEST_SCRIPT=tests.py
# debug
DEBUG=true

TEST_RESULTS=/tmp/test-results.txt
TOTAL_FAILED=0
TOTAL_SUCCESS=0
for PYTHON_VERSION in $PYTHON_VERSIONS; do
    docker pull python:$PYTHON_VERSION >/dev/null
    docker run python:$PYTHON_VERSION python --version
    docker run -v ./:/tests python:$PYTHON_VERSION rm -rf /tests/__/
    docker run -v ./:/tests python:$PYTHON_VERSION python /tests/$TEST_SCRIPT > $TEST_RESULTS 2>&1 || true
    FAILED=$(cat $TEST_RESULTS | grep FAILED | wc -l)
    SUCCESS=$(cat $TEST_RESULTS | grep SUCCESS | wc -l)
    if [ "$DEBUG" == "true" ]; then
        cat $TEST_RESULTS
    fi
    printf "SUCCESS: %2s FAILED: %2s\n" $SUCCESS $FAILED
    for SUPPORTED_PYTHON_VERSION in $SUPPORTED_PYTHON_VERSIONS; do
        if [ $PYTHON_VERSION == $SUPPORTED_PYTHON_VERSION ]; then
            TOTAL_FAILED=$((TOTAL_FAILED+$FAILED))
            TOTAL_SUCCESS=$((TOTAL_SUCCESS+$SUCCESS))
        fi
    done
done
rm $TEST_RESULTS

printf "\nTotals for supported python versions (%s): SUCCESS: %2s FAILED: %2s\n" "$SUPPORTED_PYTHON_VERSIONS" $TOTAL_SUCCESS $TOTAL_FAILED
exit $TOTAL_FAILED
