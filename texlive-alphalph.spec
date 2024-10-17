Name:		texlive-alphalph
Version:	53087
Release:	2
Summary:	Convert numbers to letters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/alphalph
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alphalph.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alphalph.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alphalph.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides commands \alphalph and \AlphAlph. They are like
\number but the expansion consists of lowercase and uppercase
letters respectively (1 to a, 26 to z, 27 to aa, 52 to zz, 53
to ba, 702 to zz, 703 to aaa, etc.). Can be used as a
replacement for LaTeX's \@alph and \@Alph macros.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/alphalph
%{_texmfdistdir}/tex/generic/alphalph
%doc %{_texmfdistdir}/doc/latex/alphalph

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
