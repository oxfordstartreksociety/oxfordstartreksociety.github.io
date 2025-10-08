Oxford Star Trek Society's Website
==================================

This is our website, check it out at
<https://oxfordstartreksociety.co.uk>.

Development Setup
-----------------

This Jekyll site requires Ruby 3.1.4. Quick setup:

```bash
# Install rbenv
brew install rbenv ruby-build
rbenv init  # follow instructions to add to shell

# Install Ruby and build
rbenv install 3.1.4
rbenv local 3.1.4
gem install bundler:2.3.26
script/build
```

**Alternative**: Use the dev container configuration for automatic setup.

List of Crews
-------------

The list of crews is stored in `_data/crews.json`. When there is a new
crew, please add yourself to the top of the list following the format
of the other crews. Ideally, you'll have a crew photo you can
provide (see the 2015-2019 crews).

License
-------
The original template for this site was taken from Start Bootstrap,
and is MIT licensed. All subsequent modifications are also MIT
licensed. See the LICENSE file for the full text.

The Oxford Star Trek Society is not endorsed, sponsored, or affiliated
with CBS Studios Inc. or the "Star Trek" franchise.  The Star Trek
trademarks, logos, and related names are owned by CBS Studios Inc.,
and are used under fair use guidelines.

The Oxford Star Trek Society is not endorsed, sponsored or affiliated
with the University of Oxford.
