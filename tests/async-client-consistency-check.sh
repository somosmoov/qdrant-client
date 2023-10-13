set -ex

# Ensure current path is project root
cd "$(dirname "$0")/../"

# Keep current version of file to check
ROOT_DIR=$(pwd)
CLIENT_DIR=$ROOT_DIR/qdrant_client
cd $CLIENT_DIR

async_files=$(ls -1 async*)

for file in $async_files ; do
    cp {,.diff.}$file
done


# Regenerate async client
$ROOT_DIR/tools/generate_async_client.sh

# Ensure generated files are the same as files in this repository
for file in $async_files ; do
    if diff -wa {,.diff.}$file
    then
        set +x
        echo "No diffs found."
    else
        set +x
        echo "ERROR: Generated $file is not consistent with file in this repository, see diff above."
        exit 1
    fi
done

# Cleanup
for file in $async_files ; do
    rm -f .diff.$file
done
