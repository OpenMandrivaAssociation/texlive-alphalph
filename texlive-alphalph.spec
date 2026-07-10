%global tl_name alphalph
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.6
Release:	%{tl_revision}.1
Summary:	Convert numbers to letters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/alphalph
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alphalph.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alphalph.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alphalph.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides commands \alphalph and \AlphAlph. They are like \number but the
expansion consists of lowercase and uppercase letters respectively (1 to
a, 26 to z, 27 to aa, 52 to zz, 53 to ba, 702 to zz, 703 to aaa, etc.).
Can be used as a replacement for LaTeX's \@alph and \@Alph macros.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/latex/alphalph
%dir %{_datadir}/texmf-dist/source/latex/alphalph
%dir %{_datadir}/texmf-dist/tex/generic/alphalph
%doc %{_datadir}/texmf-dist/doc/latex/alphalph/README.md
%doc %{_datadir}/texmf-dist/doc/latex/alphalph/alphalph.pdf
%doc %{_datadir}/texmf-dist/source/latex/alphalph/alphalph.dtx
%{_datadir}/texmf-dist/tex/generic/alphalph/alphalph.sty
