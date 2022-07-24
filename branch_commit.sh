sha=${{ github.sha }}
branch=${{ github.ref }}
name="appbalanced"

build="docker image build . -t main:$name-$branch-$sha -t latest:lastest"
eval $build