#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ff
Version  : 2.2.14
Release  : 21
URL      : https://cran.r-project.org/src/contrib/ff_2.2-14.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ff_2.2-14.tar.gz
Summary  : Memory-Efficient Storage of Large Data on Disk and Fast Access
Group    : Development/Tools
License  : GPL-2.0
Requires: R-ff-lib = %{version}-%{release}
Requires: R-bit
BuildRequires : R-bit
BuildRequires : buildreq-R

%description
Naming conventions
==================
R/x_* 		R   files extended ff (including .Rd comments)
src/x_r_ff_*	C   files extended ff
src/x_ff_*	C++ files extended ff
R/*		R   files standard ff (including .Rd comments)
src/r_ff_*	C   files standard ff
src/ff_*	C++ files standard ff
man/*.Rd	Automatically generated Rd. files, do not modify

%package lib
Summary: lib components for the R-ff package.
Group: Libraries

%description lib
lib components for the R-ff package.


%prep
%setup -q -c -n ff

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552770772

%install
export SOURCE_DATE_EPOCH=1552770772
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ff
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ff
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ff
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  ff || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ff/ANNOUNCEMENT-2.0.txt
/usr/lib64/R/library/ff/ANNOUNCEMENT-2.1.2.txt
/usr/lib64/R/library/ff/ANNOUNCEMENT-2.1.txt
/usr/lib64/R/library/ff/ANNOUNCEMENT-2.2.txt
/usr/lib64/R/library/ff/DESCRIPTION
/usr/lib64/R/library/ff/INDEX
/usr/lib64/R/library/ff/LICENSE
/usr/lib64/R/library/ff/Meta/Rd.rds
/usr/lib64/R/library/ff/Meta/features.rds
/usr/lib64/R/library/ff/Meta/hsearch.rds
/usr/lib64/R/library/ff/Meta/links.rds
/usr/lib64/R/library/ff/Meta/nsInfo.rds
/usr/lib64/R/library/ff/Meta/package.rds
/usr/lib64/R/library/ff/NAMESPACE
/usr/lib64/R/library/ff/NEWS
/usr/lib64/R/library/ff/R/ff
/usr/lib64/R/library/ff/R/ff.rdb
/usr/lib64/R/library/ff/R/ff.rdx
/usr/lib64/R/library/ff/README_devel.txt
/usr/lib64/R/library/ff/exec/make_rd.pl
/usr/lib64/R/library/ff/exec/prebuild.sh
/usr/lib64/R/library/ff/help/AnIndex
/usr/lib64/R/library/ff/help/aliases.rds
/usr/lib64/R/library/ff/help/ff.rdb
/usr/lib64/R/library/ff/help/ff.rdx
/usr/lib64/R/library/ff/help/paths.rds
/usr/lib64/R/library/ff/html/00Index.html
/usr/lib64/R/library/ff/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ff/libs/ff.so
/usr/lib64/R/library/ff/libs/ff.so.avx2
/usr/lib64/R/library/ff/libs/ff.so.avx512
