#!/usr/bin/env bash
set -e
export VERSION=$(poetry run python -c "import voting; print(voting.__version__)")
poetry build
poetry run twine upload dist/voting-${VERSION}*
git tag -a ${VERSION} -m "${VERSION}"
git push --tags