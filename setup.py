#!/usr/bin/env python
from setuptools import find_packages
from setuptools import setup

package_name = "dbt-cdp-salesforce"
package_version = "0.0.1"
description = """The salesforce cdp adapter plugin for dbt (data build tool)"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    author="Supriya-Srishti",
    author_email="sjahagirdar@salesforce.com",
    url="https://github.com/forcedotcom/Salesforce-CDP-jdbc",
    packages=find_packages(),
    package_data={
        'dbt': [
            'include/myadapter/macros/*.sql',
            'include/myadapter/dbt_project.yml',
        ]
    },
    install_requires=[
        "dbt-core==0.19.1",
        "JayDeBeApi==1.2.3"
    ]
)
