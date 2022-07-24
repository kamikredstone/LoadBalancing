sha=${{ github.sha }}
branch=${{ github.ref }}
name="appbalanced"

build="docker image build . -t kamikredstone/ptecr:$name-$branch-$sha -t kamikredstone/ptecr:lastest"
eval $build
