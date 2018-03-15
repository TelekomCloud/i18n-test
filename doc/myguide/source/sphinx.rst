Sphinx
======

Sphinx, the Python Documentation Generator, provides `Internationalization <http://www.sphinx-doc.org/en/stable/intl.html>`__
. The workflow is described :ref:`there <sphinx:intl>`.

btw: documentation reference can be build with :ref:`intersphinx <sphinx:examples>`
Check available options::

    python -m sphinx.ext.intersphinx 'http://www.sphinx-doc.org/en/master/objects.inv'

Install requirements::

    pip install -r requirements.txt

To initial a new documentation project use::

    sphinx-quickstart

To interact to Zanata server with the client a project configuration
file is required::

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <config xmlns="http://zanata.org/namespace/config/">
      <url>https://zanata.lxd/</url>
      <project>myrepo</project>
      <project-version>master</project-version>
      <project-type>gettext</project-type>
      <src-dir>.</src-dir>
      <trans-dir>.</trans-dir>
      <rules>
        <rule pattern="**/*.pot">{path}/{locale_with_underscore}/LC_MESSAGES/{filename}.po</rule>
      </rules>
    </config>

url must match with url name in zanata.ini

Build gettext files for Zanata::

    sphinx-build -b gettext doc/myguide/source/ doc/myguide/source/locale/

Push pot files to Zanata::

    zanata-cli -e push --disable-ssl-cert

Normaly self-signed certificate will used in private environment like
this. The option --disable-ssl-cert will force the client to connect.

Now the translation files are on the server and translatable in the
configured languages. If this done you can download it again::

    zanata-cli -e pull -l de  --disable-ssl-cert

Use language option -l de for German files, without that all
language files will be download.

Optional: If you modified the language files locally, you can push
them to the server::

    zanata-cli -e push --push-type trans --disable-ssl-cert

At the and, build and publish the docs::

    sphinx-build -b html doc/myguide/source/ doc/myguide/build/html/en
    sphinx-build -b html doc/myguide/source/ doc/myguide/build/html/de -D language='de'

