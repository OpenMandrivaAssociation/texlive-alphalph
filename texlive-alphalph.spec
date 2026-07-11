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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides commands \alphalph and \AlphAlph. They are like \number but the
expansion consists of lowercase and uppercase letters respectively (1 to
a, 26 to z, 27 to aa, 52 to zz, 53 to ba, 702 to zz, 703 to aaa, etc.).
Can be used as a replacement for LaTeX's \@alph and \@Alph macros.

