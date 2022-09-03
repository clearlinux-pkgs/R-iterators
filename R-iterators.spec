#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-iterators
Version  : 1.0.14
Release  : 68
URL      : https://cran.r-project.org/src/contrib/iterators_1.0.14.tar.gz
Source0  : https://cran.r-project.org/src/contrib/iterators_1.0.14.tar.gz
Summary  : Provides Iterator Construct
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : buildreq-R

%description
through all the elements of a vector, list, or other collection of data.

%prep
%setup -q -c -n iterators
cd %{_builddir}/iterators

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644184303

%install
export SOURCE_DATE_EPOCH=1644184303
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library iterators
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library iterators
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library iterators
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc iterators || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/iterators/DESCRIPTION
/usr/lib64/R/library/iterators/INDEX
/usr/lib64/R/library/iterators/Meta/Rd.rds
/usr/lib64/R/library/iterators/Meta/features.rds
/usr/lib64/R/library/iterators/Meta/hsearch.rds
/usr/lib64/R/library/iterators/Meta/links.rds
/usr/lib64/R/library/iterators/Meta/nsInfo.rds
/usr/lib64/R/library/iterators/Meta/package.rds
/usr/lib64/R/library/iterators/Meta/vignette.rds
/usr/lib64/R/library/iterators/NAMESPACE
/usr/lib64/R/library/iterators/NEWS.md
/usr/lib64/R/library/iterators/R/iterators
/usr/lib64/R/library/iterators/R/iterators.rdb
/usr/lib64/R/library/iterators/R/iterators.rdx
/usr/lib64/R/library/iterators/doc/index.html
/usr/lib64/R/library/iterators/doc/iterators.R
/usr/lib64/R/library/iterators/doc/iterators.Rnw
/usr/lib64/R/library/iterators/doc/iterators.pdf
/usr/lib64/R/library/iterators/doc/writing.R
/usr/lib64/R/library/iterators/doc/writing.Rnw
/usr/lib64/R/library/iterators/doc/writing.pdf
/usr/lib64/R/library/iterators/examples/ifilter.R
/usr/lib64/R/library/iterators/examples/iforever.R
/usr/lib64/R/library/iterators/examples/ihasNext.R
/usr/lib64/R/library/iterators/examples/ilimit.R
/usr/lib64/R/library/iterators/examples/ipermn.R
/usr/lib64/R/library/iterators/examples/irecycle.R
/usr/lib64/R/library/iterators/examples/irep.R
/usr/lib64/R/library/iterators/examples/iseq.R
/usr/lib64/R/library/iterators/examples/itimer.R
/usr/lib64/R/library/iterators/examples/ivector.R
/usr/lib64/R/library/iterators/examples/ivector2.R
/usr/lib64/R/library/iterators/help/AnIndex
/usr/lib64/R/library/iterators/help/aliases.rds
/usr/lib64/R/library/iterators/help/iterators.rdb
/usr/lib64/R/library/iterators/help/iterators.rdx
/usr/lib64/R/library/iterators/help/paths.rds
/usr/lib64/R/library/iterators/html/00Index.html
/usr/lib64/R/library/iterators/html/R.css
/usr/lib64/R/library/iterators/tests/doRUnit.R
/usr/lib64/R/library/iterators/unitTests/basicTest.R
/usr/lib64/R/library/iterators/unitTests/chunksizeTest.R
/usr/lib64/R/library/iterators/unitTests/iapplyTest.R
/usr/lib64/R/library/iterators/unitTests/icountnTest.R
/usr/lib64/R/library/iterators/unitTests/isplitTest.R
/usr/lib64/R/library/iterators/unitTests/recycleTest.R
/usr/lib64/R/library/iterators/unitTests/runTestSuite.sh
