% Copyright (c) 2015, BENCHOP, Slobodan Milovanović
% All rights reserved.
% This MATLAB code has been written for the BENCHOP project.
% Redistribution and use in source and binary forms, with or without
% modification, are permitted provided that the following conditions are
% met:
%    * Redistributions of source code must retain the above copyright
%       notice, this list of conditions and the following disclaimer.
%    * Redistributions in binary form must reproduce the above copyright
%       notice, this list of conditions and the following disclaimer in
%       the documentation and/or other materials provided with the distribution
%    * BENCHOP article is properly cited by the user of the BENCHOP codes when publishing/reporting related scientific results.
% 
% THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
% AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
% IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
% ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
% LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
% CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
% SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
% INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
% CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
% ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
% POSSIBILITY OF SUCH DAMAGE.


% Problems:
% P1aI
% P1bI
% P1cI
% P1aII
% P1bII
% P1cII

% Methods:
% COS
% RBFFD
% UniformGrid

function [time, relerr] = singleMethod(problem, method, params)
    if strcmp(method, 'COS') || strcmp(method, 'RBFFD') || strcmp(method, 'UniformGrid')
        methodPath = strcat(method, '.m');
    else
        return
    end

    %% Problem 1 a) I
    if strcmp(problem, 'P1aI')
        rootpath=pwd;
        U=[2.758443856146076 7.485087593912603 14.702019669720769];

        filepathsBSeuCallUI=getfilenames('./',strcat('BSeuCallUI_', methodPath));
        par={S,K,T,r,sig};
        [timeBSeuCallUI,relerrBSeuCallUI] = executor(rootpath,filepathsBSeuCallUI,U,par);

        time=timeBSeuCallUI(1);
        relerr=relerrBSeuCallUI(1);
    
    %% Problem 1 b) I
    elseif strcmp(problem, 'P1bI')
        rootpath=pwd;
        S=[90,100,110]; K=100; T=1.0; r=0.03;
        U=[10.726486710094511 4.820608184813253 1.828207584020458];

        filepathsBSamPutUI=getfilenames('./',strcat('BSamPutUI_', methodPath));
        par={S,K,T,r,sig};
        [timeBSamPutUI,relerrBSamPutUI] = executor(rootpath,filepathsBSamPutUI,U,par);

        time=timeBSamPutUI;
        relerr=relerrBSamPutUI;

    %% Problem 1 c) I
    elseif strcmp(problem, 'P1cI')
        rootpath=pwd;
        S=[90,100,110]; K=100; T=1.0; r=0.03; B=1.25*K;
        U=[1.822512255945242 3.294086516281595 3.221591131246868];

        filepathsBSupoutCallI=getfilenames('./',strcat('BSupoutCallI_', methodPath));
        par={S,K,T,r,sig,B};
        [timeBSupoutCallI,relerrBSupoutCallI] = executor(rootpath,filepathsBSupoutCallI,U,par);

        time=timeBSupoutCallI;
        relerr=relerrBSupoutCallI;
    
    %% Problem 1 a) II
    elseif strcmp(problem, 'P1aII')
        rootpath=pwd;
        S=[97,98,99]; r=0.1; T=0.25; K=100;
        U=[0.033913177006141   0.512978189232598   1.469203342553328];

        filepathsBSeuCallUII=getfilenames('./',strcat('BSeuCallUII_', methodPath));
        par={S,K,T,r,sig};
        [timeBSeuCallUII,relerrBSeuCallUII] = executor(rootpath,filepathsBSeuCallUII,U,par);

        time=timeBSeuCallUII;
        relerr=relerrBSeuCallUII;

    %% Problem 1 b) II
    elseif strcmp(problem, 'P1bII')
        rootpath=pwd;
        S=[97,98,99]; K=100; T=0.25; r=0.1;
        U=[3.000000000000682 2.000000000010786   1.000000000010715];

        filepathsBSamPutUII=getfilenames('./',strcat('BSamPutUII_', methodPath));
        par={S,K,T,r,sig};
        [timeBSamPutUII,relerrBSamPutUII] = executor(rootpath,filepathsBSamPutUII,U,par);

        time=timeBSamPutUII;
        relerr=relerrBSamPutUII;

    %% Problem 1 c) II
    elseif strcmp(problem, 'P1cII')
        rootpath=pwd;
        S=[97,98,99]; r=0.1; T=0.25; K=100; B=1.25*K;
        U=[0.033913177006134   0.512978189232598   1.469203342553328];

        filepathsBSupoutCallII=getfilenames('./',strcat('BSupoutCallII_', methodPath));
        par={S,K,T,r,sig,B};
        [timeBSupoutCallII,relerrBSupoutCallII] = executor(rootpath,filepathsBSupoutCallII,U,par);

        time=timeBSupoutCallII;
        relerr=relerrBSupoutCallII;
    end
