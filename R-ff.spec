#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v20
# autospec commit: f35655a
#
Name     : R-ff
Version  : 4.5.0
Release  : 58
URL      : https://cran.r-project.org/src/contrib/ff_4.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ff_4.5.0.tar.gz
Summary  : Memory-Efficient Storage of Large Data on Disk and Fast Access
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-ff-lib = %{version}-%{release}
Requires: R-bit
BuildRequires : R-bit
BuildRequires : buildreq-R

%description
disk but behave (almost) as if they were in RAM by transparently 
	mapping only a section (pagesize) in main memory - the effective 
	virtual memory consumption per ff object. ff supports R's standard 
	atomic data types 'double', 'logical', 'raw' and 'integer' and 
	non-standard atomic types boolean (1 bit), quad (2 bit unsigned), 
	nibble (4 bit unsigned), byte (1 byte signed with NAs), ubyte (1 byte 
	unsigned), short (2 byte signed with NAs), ushort (2 byte unsigned), 
	single (4 byte float with NAs). For example 'quad' allows efficient 
	storage of genomic data as an 'A','T','G','C' factor. The unsigned 
	types support 'circular' arithmetic. There is also support for 
	close-to-atomic types 'factor', 'ordered', 'POSIXct', 'Date' and 
	custom close-to-atomic types. 
	ff not only has native C-support for vectors, matrices and arrays 
	with flexible dimorder (major column-order, major row-order and 
	generalizations for arrays). There is also a ffdf class not unlike 
	data.frames and import/export filters for csv files.
	ff objects store raw data in binary flat files in native encoding,
	and complement this with metadata stored in R as physical and virtual
	attributes. ff objects have well-defined hybrid copying semantics, 
	which gives rise to certain performance improvements through 
	virtualization. ff objects can be stored and reopened across R 
	sessions. ff files can be shared by multiple ff R objects 
	(using different data en/de-coding schemes) in the same process 
	or from multiple R processes to exploit parallelism. A wide choice of 
	finalizer options allows to work with 'permanent' files as well as 
	creating/removing 'temporary' ff files completely transparent to the 
	user. On certain OS/Filesystem combinations, creating the ff files
	works without notable delay thanks to using sparse file allocation.
	Several access optimization techniques such as Hybrid Index 
	Preprocessing and Virtualization are implemented to achieve good 
	performance even with large datasets, for example virtual matrix 
	transpose without touching a single byte on disk. Further, to reduce 
	disk I/O, 'logicals' and non-standard data types get stored native and 
	compact on binary flat files i.e. logicals take up exactly 2 bits to 
	represent TRUE, FALSE and NA. 
	Beyond basic access functions, the ff package also provides 
	compatibility functions that facilitate writing code for ff and ram 
	objects and support for batch processing on ff objects (e.g. as.ram, 
	as.ff, ffapply). ff interfaces closely with functionality from package

%package lib
Summary: lib components for the R-ff package.
Group: Libraries

%description lib
lib components for the R-ff package.


%prep
%setup -q -n ff
pushd ..
cp -a ff buildavx2
popd
pushd ..
cp -a ff buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726852471

%install
export SOURCE_DATE_EPOCH=1726852471
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
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
/usr/lib64/R/library/ff/exec/make_rd.pl
/usr/lib64/R/library/ff/exec/prebuild.sh
/usr/lib64/R/library/ff/help/AnIndex
/usr/lib64/R/library/ff/help/aliases.rds
/usr/lib64/R/library/ff/help/ff.rdb
/usr/lib64/R/library/ff/help/ff.rdx
/usr/lib64/R/library/ff/help/paths.rds
/usr/lib64/R/library/ff/html/00Index.html
/usr/lib64/R/library/ff/html/R.css
/usr/lib64/R/library/ff/tests/testthat.R
/usr/lib64/R/library/ff/tests/testthat/test-zeroRows.R
/usr/lib64/R/library/ff/tests/testthat/test-zero_lengths.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/ff/libs/ff.so
/V4/usr/lib64/R/library/ff/libs/ff.so
/usr/lib64/R/library/ff/libs/ff.so
