# -*- coding: utf-8 -*-
#
# Copyright 2011-2018 Matt Austin
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from fabric.api import lcd, local, task
import os


local_pwd = os.path.realpath(os.path.dirname(os.path.realpath(__file__)))

project_name = os.path.split(local_pwd)[-1]


@task
def build():
    with lcd('.'):
        local('docker build --tag="{}" .'.format(project_name))


@task
def remove_pyc_files():
    local('find . -name \'*.pyc\' -delete')


@task
def run(command='check'):
    with lcd('.'):
        local('docker run --user {uid}:{gid} --rm --tty --interactive '
              '--shm-size 2g '
              '--volume={local_pwd}:/var/task '
              '--volume=/tmp/django-thummer:/tmp/django-thummer '
              '{project_name} {command}'.format(
                  uid=os.getuid(), gid=os.getgid(), local_pwd=local_pwd,
                  project_name=project_name, command=command))


@task
def test():
    return run(command='test')
