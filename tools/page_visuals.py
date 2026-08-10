"""Per-page hero visuals. Each returns the inner SVG for a 460x460 panel."""

SERVICES = """
              <circle class="hv-orbit" cx="230" cy="200" r="196" fill="none" stroke="url(#hvGrad)"
                stroke-opacity=".4" stroke-width="1.3" stroke-dasharray="3 12"></circle>

              <!-- delivery pipeline: build -> publish -> support -->
              <g class="hv-links" stroke="url(#hvGrad)" stroke-width="2" fill="none" stroke-linecap="round">
                <path id="svL1" class="hv-link" d="M148 118 H312"></path>
                <path id="svL2" class="hv-link" d="M148 214 H312" style="animation-delay:.6s"></path>
                <path id="svL3" class="hv-link" d="M148 310 H312" style="animation-delay:1.2s"></path>
              </g>
              <circle r="3.6" fill="#f6c90e">
                <animateMotion dur="2.8s" repeatCount="indefinite"><mpath href="#svL1"></mpath></animateMotion>
              </circle>
              <circle r="3.6" fill="#ffb000">
                <animateMotion dur="2.8s" begin=".55s" repeatCount="indefinite"><mpath href="#svL2"></mpath></animateMotion>
              </circle>
              <circle r="3.6" fill="#fff3b0">
                <animateMotion dur="2.8s" begin="1.1s" repeatCount="indefinite"><mpath href="#svL3"></mpath></animateMotion>
              </circle>

              <g class="hv-icon">
                <circle class="hv-halo" cx="118" cy="118" r="32" fill="#f6c90e" opacity=".2"></circle>
                <circle cx="118" cy="118" r="30" fill="#1a1810" stroke="#f6c90e" stroke-opacity=".45" stroke-width="1.4"></circle>
                <g transform="translate(118 118)" stroke="#f6c90e" stroke-width="2.4" fill="none"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path d="M-3 -7 L-11 0 L-3 7"></path>
                  <path d="M3 -7 L11 0 L3 7"></path>
                </g>
                <text class="hv-label" x="118" y="166">Build</text>
              </g>
              <g class="hv-icon" style="animation-delay:1.2s">
                <circle class="hv-halo" cx="342" cy="118" r="32" fill="#ffb000" opacity=".18" style="animation-delay:.7s"></circle>
                <circle cx="342" cy="118" r="30" fill="#1a1810" stroke="#f6c90e" stroke-opacity=".45" stroke-width="1.4"></circle>
                <g transform="translate(342 118)">
                  <rect x="-11" y="-9" width="22" height="18" rx="2.6" fill="none" stroke="#f6c90e" stroke-width="1.8"></rect>
                  <path d="M-11 -3.4 H11" stroke="#f6c90e" stroke-width="1.8"></path>
                  <circle cx="-7.6" cy="-6.2" r="1.1" fill="#f6c90e"></circle>
                  <circle cx="-4.2" cy="-6.2" r="1.1" fill="#f6c90e"></circle>
                </g>
                <text class="hv-label" x="342" y="166">Web</text>
              </g>

              <g class="hv-icon" style="animation-delay:2.4s">
                <circle class="hv-halo" cx="118" cy="214" r="32" fill="#fff3b0" opacity=".16" style="animation-delay:1.4s"></circle>
                <circle cx="118" cy="214" r="30" fill="#1a1810" stroke="#f6c90e" stroke-opacity=".45" stroke-width="1.4"></circle>
                <g transform="translate(118 214)">
                  <rect x="-7.5" y="-11" width="15" height="22" rx="2.6" fill="none" stroke="#f6c90e" stroke-width="1.8"></rect>
                  <circle cx="0" cy="7" r="1.5" fill="#f6c90e"></circle>
                </g>
                <text class="hv-label" x="118" y="262">Apps</text>
              </g>
              <g class="hv-icon" style="animation-delay:3.6s">
                <circle class="hv-halo" cx="342" cy="214" r="32" fill="#f6c90e" opacity=".18" style="animation-delay:2.1s"></circle>
                <circle cx="342" cy="214" r="30" fill="#1a1810" stroke="#f6c90e" stroke-opacity=".45" stroke-width="1.4"></circle>
                <g transform="translate(342 214)">
                  <rect x="-11" y="-8" width="22" height="16" rx="3" fill="none" stroke="#f6c90e" stroke-width="1.8"></rect>
                  <path d="M-2.4 -4.4 L5.2 0 L-2.4 4.4 Z" fill="#f6c90e"></path>
                </g>
                <text class="hv-label" x="342" y="262">Content</text>
              </g>

              <g class="hv-icon" style="animation-delay:4.8s">
                <circle class="hv-halo" cx="118" cy="310" r="32" fill="#ffb000" opacity=".18" style="animation-delay:2.8s"></circle>
                <circle cx="118" cy="310" r="30" fill="#1a1810" stroke="#f6c90e" stroke-opacity=".45" stroke-width="1.4"></circle>
                <g transform="translate(118 310)" fill="#f6c90e">
                  <circle cx="-4.5" cy="1.5" r="4.6"></circle>
                  <circle cx="1.6" cy="-2.2" r="6"></circle>
                  <circle cx="7.4" cy="2" r="4.2"></circle>
                  <rect x="-4.5" y="1.6" width="12" height="4.6" rx="2.3"></rect>
                  <path d="M1.6 -12 L1.6 -20 M-2.4 -16.4 L1.6 -20.4 L5.6 -16.4" stroke="#f6c90e"
                    stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"></path>
                </g>
                <text class="hv-label" x="118" y="358">Deploy</text>
              </g>
              <g class="hv-icon" style="animation-delay:6s">
                <circle class="hv-halo" cx="342" cy="310" r="32" fill="#fff3b0" opacity=".16" style="animation-delay:3.5s"></circle>
                <circle cx="342" cy="310" r="30" fill="#1a1810" stroke="#f6c90e" stroke-opacity=".45" stroke-width="1.4"></circle>
                <g transform="translate(342 310)" stroke="#f6c90e" stroke-width="2" fill="none" stroke-linecap="round">
                  <path d="M-11 2 L-5 2 L-2 -7 L3 9 L6 2 L11 2">
                    <animate attributeName="stroke-dasharray" values="0 46;46 0" dur="2.4s" repeatCount="indefinite"></animate>
                  </path>
                </g>
                <text class="hv-label" x="342" y="358">Monitor</text>
              </g>
"""

CLOUD = """
              <circle class="hv-orbit" cx="230" cy="150" r="128" fill="none" stroke="url(#hvGrad)"
                stroke-opacity=".38" stroke-width="1.3" stroke-dasharray="3 12"></circle>

              <!-- the cloud -->
              <g class="hv-icon">
                <circle class="hv-halo" cx="230" cy="146" r="66" fill="#f6c90e" opacity=".16"></circle>
                <g transform="translate(230 146)" fill="#f6c90e">
                  <circle cx="-24" cy="8" r="22"></circle>
                  <circle cx="4" cy="-6" r="30"></circle>
                  <circle cx="30" cy="10" r="20"></circle>
                  <rect x="-24" y="8" width="54" height="20" rx="10"></rect>
                </g>
                <g transform="translate(230 146)" fill="#1a1810" stroke="none">
                  <path d="M-9 4 L-1 4 L-1 -8 L9 6 L1 6 L1 18 Z" opacity=".9"></path>
                </g>
              </g>

              <!-- uplinks from the racks -->
              <g stroke="url(#hvGrad)" stroke-width="2" fill="none" stroke-linecap="round">
                <path id="clL1" class="hv-link" d="M112 300 L196 196"></path>
                <path id="clL2" class="hv-link" d="M230 306 L230 200" style="animation-delay:.5s"></path>
                <path id="clL3" class="hv-link" d="M348 300 L264 196" style="animation-delay:1s"></path>
              </g>
              <circle r="3.6" fill="#f6c90e">
                <animateMotion dur="2.4s" repeatCount="indefinite"><mpath href="#clL1"></mpath></animateMotion>
              </circle>
              <circle r="3.6" fill="#ffb000">
                <animateMotion dur="2.4s" begin=".5s" repeatCount="indefinite"><mpath href="#clL2"></mpath></animateMotion>
              </circle>
              <circle r="3.6" fill="#fff3b0">
                <animateMotion dur="2.4s" begin="1s" repeatCount="indefinite"><mpath href="#clL3"></mpath></animateMotion>
              </circle>

              <!-- server racks -->
              <g class="hv-icon" style="animation-delay:.4s">
                <rect x="76" y="304" width="72" height="76" rx="10" fill="#1a1810" stroke="#f6c90e"
                  stroke-opacity=".45" stroke-width="1.4"></rect>
                <g stroke="#f6c90e" stroke-width="2" stroke-linecap="round">
                  <path d="M92 322 H132"></path>
                  <path d="M92 342 H132"></path>
                  <path d="M92 362 H132"></path>
                </g>
                <circle cx="136" cy="322" r="2.6" fill="#fff3b0">
                  <animate attributeName="opacity" values="1;.2;1" dur="1.8s" repeatCount="indefinite"></animate>
                </circle>
                <text class="hv-label" x="112" y="400">Config</text>
              </g>
              <g class="hv-icon" style="animation-delay:1.5s">
                <rect x="194" y="304" width="72" height="76" rx="10" fill="#1a1810" stroke="#f6c90e"
                  stroke-opacity=".45" stroke-width="1.4"></rect>
                <g stroke="#f6c90e" stroke-width="2" stroke-linecap="round">
                  <path d="M210 322 H250"></path>
                  <path d="M210 342 H250"></path>
                  <path d="M210 362 H250"></path>
                </g>
                <circle cx="254" cy="342" r="2.6" fill="#fff3b0">
                  <animate attributeName="opacity" values="1;.2;1" dur="1.8s" begin=".6s" repeatCount="indefinite"></animate>
                </circle>
                <text class="hv-label" x="230" y="400">Deploy</text>
              </g>
              <g class="hv-icon" style="animation-delay:2.6s">
                <rect x="312" y="304" width="72" height="76" rx="10" fill="#1a1810" stroke="#f6c90e"
                  stroke-opacity=".45" stroke-width="1.4"></rect>
                <g stroke="#f6c90e" stroke-width="2" stroke-linecap="round">
                  <path d="M328 322 H368"></path>
                  <path d="M328 342 H368"></path>
                  <path d="M328 362 H368"></path>
                </g>
                <circle cx="372" cy="362" r="2.6" fill="#fff3b0">
                  <animate attributeName="opacity" values="1;.2;1" dur="1.8s" begin="1.2s" repeatCount="indefinite"></animate>
                </circle>
                <text class="hv-label" x="348" y="400">Maintain</text>
              </g>
"""

SUPPORT = """
              <!-- uptime panel -->
              <rect x="52" y="86" width="356" height="196" rx="16" fill="#1a1810" stroke="#f6c90e"
                stroke-opacity=".4" stroke-width="1.4"></rect>
              <text class="hv-label" x="90" y="118" style="text-anchor:start">Uptime</text>
              <circle cx="352" cy="112" r="5" fill="#f6c90e">
                <animate attributeName="opacity" values="1;.25;1" dur="1.6s" repeatCount="indefinite"></animate>
              </circle>
              <text class="hv-label" x="336" y="116" style="text-anchor:end">Live</text>

              <g stroke="#ffffff" stroke-opacity=".08" stroke-width="1">
                <path d="M52 160 H408"></path>
                <path d="M52 206 H408"></path>
                <path d="M52 252 H408"></path>
              </g>

              <path id="spTrend" fill="none" stroke="url(#hvGrad)" stroke-width="3" stroke-linecap="round"
                stroke-linejoin="round"
                d="M76 244 L118 214 L156 232 L196 176 L236 200 L276 148 L316 172 L384 128">
                <animate attributeName="stroke-dasharray" values="0 460;460 0" dur="3.2s"
                  repeatCount="indefinite"></animate>
              </path>
              <circle r="4.6" fill="#fff3b0">
                <animateMotion dur="3.2s" repeatCount="indefinite"><mpath href="#spTrend"></mpath></animateMotion>
              </circle>

              <!-- checks clearing -->
              <g class="hv-icon">
                <rect x="52" y="308" width="356" height="42" rx="10" fill="#1a1810" stroke="#f6c90e"
                  stroke-opacity=".3" stroke-width="1.2"></rect>
                <circle cx="82" cy="329" r="10" fill="none" stroke="#f6c90e" stroke-width="1.8"></circle>
                <path d="M77 329 L81 333 L88 325" fill="none" stroke="#f6c90e" stroke-width="2.2"
                  stroke-linecap="round" stroke-linejoin="round">
                  <animate attributeName="stroke-dasharray" values="0 18;18 0" dur="2.4s" repeatCount="indefinite"></animate>
                </path>
                <text class="hv-label" x="106" y="334" style="text-anchor:start">Issue checked</text>
              </g>
              <g class="hv-icon" style="animation-delay:1.6s">
                <rect x="52" y="360" width="356" height="42" rx="10" fill="#1a1810" stroke="#f6c90e"
                  stroke-opacity=".3" stroke-width="1.2"></rect>
                <circle cx="82" cy="381" r="10" fill="none" stroke="#f6c90e" stroke-width="1.8"></circle>
                <path d="M77 381 L81 385 L88 377" fill="none" stroke="#f6c90e" stroke-width="2.2"
                  stroke-linecap="round" stroke-linejoin="round">
                  <animate attributeName="stroke-dasharray" values="0 18;18 0" dur="2.4s" begin="1.2s"
                    repeatCount="indefinite"></animate>
                </path>
                <text class="hv-label" x="106" y="386" style="text-anchor:start">Release verified</text>
              </g>
"""

COURSES = """
              <circle class="hv-orbit" cx="230" cy="212" r="196" fill="none" stroke="url(#hvGrad)"
                stroke-opacity=".34" stroke-width="1.3" stroke-dasharray="3 12"></circle>

              <!-- progress rings, one per course -->
              <g transform="translate(112 176)">
                <circle r="46" fill="none" stroke="#ffffff" stroke-opacity=".1" stroke-width="7"></circle>
                <circle r="46" fill="none" stroke="#f6c90e" stroke-width="7" stroke-linecap="round"
                  transform="rotate(-90)" stroke-dasharray="289" stroke-dashoffset="289">
                  <animate attributeName="stroke-dashoffset" values="289;72;72;289" dur="6s"
                    repeatCount="indefinite"></animate>
                </circle>
                <text class="hv-label" y="5" style="font-size:13px;fill:rgba(255,255,255,.82)">PY</text>
              </g>
              <text class="hv-label" x="112" y="248">Python</text>

              <g transform="translate(230 274)">
                <circle r="46" fill="none" stroke="#ffffff" stroke-opacity=".1" stroke-width="7"></circle>
                <circle r="46" fill="none" stroke="#ffb000" stroke-width="7" stroke-linecap="round"
                  transform="rotate(-90)" stroke-dasharray="289" stroke-dashoffset="289">
                  <animate attributeName="stroke-dashoffset" values="289;40;40;289" dur="6s" begin=".8s"
                    repeatCount="indefinite"></animate>
                </circle>
                <text class="hv-label" y="5" style="font-size:13px;fill:rgba(255,255,255,.82)">AI</text>
              </g>
              <text class="hv-label" x="230" y="346">AI tools</text>

              <g transform="translate(348 176)">
                <circle r="46" fill="none" stroke="#ffffff" stroke-opacity=".1" stroke-width="7"></circle>
                <circle r="46" fill="none" stroke="#fff3b0" stroke-width="7" stroke-linecap="round"
                  transform="rotate(-90)" stroke-dasharray="289" stroke-dashoffset="289">
                  <animate attributeName="stroke-dashoffset" values="289;96;96;289" dur="6s" begin="1.6s"
                    repeatCount="indefinite"></animate>
                </circle>
                <text class="hv-label" y="5" style="font-size:13px;fill:rgba(255,255,255,.82)">WS</text>
              </g>
              <text class="hv-label" x="348" y="248">Workspace</text>

              <!-- graduation cap -->
              <g class="hv-icon">
                <path d="M230 74 L292 100 L230 126 L168 100 Z" fill="#f6c90e"></path>
                <path d="M196 112 V134 C196 146, 264 146, 264 134 V112" fill="none" stroke="#f6c90e"
                  stroke-width="3" stroke-linecap="round"></path>
                <path d="M292 100 V128" stroke="#f6c90e" stroke-width="2.4" stroke-linecap="round"></path>
                <circle cx="292" cy="132" r="4" fill="#f6c90e">
                  <animate attributeName="cy" values="132;138;132" dur="2.6s" repeatCount="indefinite"></animate>
                </circle>
              </g>
"""

CAREERS = """
              <circle class="hv-orbit" cx="230" cy="216" r="190" fill="none" stroke="url(#hvGrad)"
                stroke-opacity=".36" stroke-width="1.3" stroke-dasharray="3 12"></circle>

              <g stroke="url(#hvGrad)" stroke-width="1.8" fill="none" stroke-linecap="round">
                <path id="crL1" class="hv-link" d="M198 190 L146 152"></path>
                <path id="crL2" class="hv-link" d="M262 190 L314 152" style="animation-delay:.5s"></path>
                <path id="crL3" class="hv-link" d="M198 242 L146 280" style="animation-delay:1s"></path>
                <path id="crL4" class="hv-link" d="M262 242 L314 280" style="animation-delay:1.5s"></path>
              </g>
              <circle r="3.4" fill="#f6c90e">
                <animateMotion dur="2.4s" repeatCount="indefinite"><mpath href="#crL1"></mpath></animateMotion>
              </circle>
              <circle r="3.4" fill="#ffb000">
                <animateMotion dur="2.4s" begin=".5s" repeatCount="indefinite"><mpath href="#crL2"></mpath></animateMotion>
              </circle>
              <circle r="3.4" fill="#fff3b0">
                <animateMotion dur="2.4s" begin="1s" repeatCount="indefinite"><mpath href="#crL3"></mpath></animateMotion>
              </circle>
              <circle r="3.4" fill="#f6c90e">
                <animateMotion dur="2.4s" begin="1.5s" repeatCount="indefinite"><mpath href="#crL4"></mpath></animateMotion>
              </circle>

              <!-- the team -->
              <circle class="hv-core-ring" cx="230" cy="216" r="62" fill="none" stroke="url(#hvGrad)"
                stroke-opacity=".5" stroke-width="1.4" stroke-dasharray="14 9"></circle>
              <circle class="hv-halo" cx="230" cy="216" r="50" fill="#f6c90e" opacity=".16"></circle>
              <circle cx="230" cy="216" r="48" fill="#1a1810" stroke="#f6c90e" stroke-opacity=".45"
                stroke-width="1.4"></circle>
              <g transform="translate(230 216)" fill="#f6c90e">
                <circle cx="-9" cy="-6" r="6.4"></circle>
                <circle cx="9" cy="-6" r="6.4"></circle>
                <path d="M-22 12 C-22 2, -16 -1, -9 -1 C-2 -1, 4 2, 4 12 Z"></path>
                <path d="M-4 12 C-4 2, 2 -1, 9 -1 C16 -1, 22 2, 22 12 Z" opacity=".75"></path>
              </g>

              <!-- the four open roles -->
              <g class="hv-icon">
                <circle class="hv-halo" cx="118" cy="128" r="30" fill="#f6c90e" opacity=".2"></circle>
                <circle cx="118" cy="128" r="28" fill="#1a1810" stroke="#f6c90e" stroke-opacity=".45" stroke-width="1.4"></circle>
                <g transform="translate(118 128)" fill="none" stroke="#f6c90e" stroke-width="1.8">
                  <ellipse rx="12" ry="4.6"></ellipse>
                  <ellipse rx="12" ry="4.6" transform="rotate(60)"></ellipse>
                  <ellipse rx="12" ry="4.6" transform="rotate(120)"></ellipse>
                  <circle r="2.4" fill="#f6c90e" stroke="none"></circle>
                </g>
                <text class="hv-label" x="118" y="176">React N.</text>
              </g>
              <g class="hv-icon" style="animation-delay:1.4s">
                <circle class="hv-halo" cx="342" cy="128" r="30" fill="#ffb000" opacity=".18" style="animation-delay:.8s"></circle>
                <circle cx="342" cy="128" r="28" fill="#1a1810" stroke="#f6c90e" stroke-opacity=".45" stroke-width="1.4"></circle>
                <g transform="translate(342 128)" fill="#f6c90e">
                  <path d="M2 -12 L-10 0 L-4 6 L14 -12 Z"></path>
                  <path d="M2 12 L-4 6 L2 0 L14 12 Z" opacity=".75"></path>
                </g>
                <text class="hv-label" x="342" y="176">Flutter</text>
              </g>
              <g class="hv-icon" style="animation-delay:2.8s">
                <circle class="hv-halo" cx="118" cy="304" r="30" fill="#fff3b0" opacity=".16" style="animation-delay:1.6s"></circle>
                <circle cx="118" cy="304" r="28" fill="#1a1810" stroke="#f6c90e" stroke-opacity=".45" stroke-width="1.4"></circle>
                <g transform="translate(118 304)" stroke="#f6c90e" stroke-width="2.2" fill="none"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path d="M-3 -7 L-11 0 L-3 7"></path>
                  <path d="M3 -7 L11 0 L3 7"></path>
                </g>
                <text class="hv-label" x="118" y="352">Web</text>
              </g>
              <g class="hv-icon" style="animation-delay:4.2s">
                <circle class="hv-halo" cx="342" cy="304" r="30" fill="#f6c90e" opacity=".18" style="animation-delay:2.4s"></circle>
                <circle cx="342" cy="304" r="28" fill="#1a1810" stroke="#f6c90e" stroke-opacity=".45" stroke-width="1.4"></circle>
                <g transform="translate(342 304)" fill="#f6c90e">
                  <circle cx="-4.5" cy="1.5" r="4.6"></circle>
                  <circle cx="1.6" cy="-2.2" r="6"></circle>
                  <circle cx="7.4" cy="2" r="4.2"></circle>
                  <rect x="-4.5" y="1.6" width="12" height="4.6" rx="2.3"></rect>
                </g>
                <text class="hv-label" x="342" y="352">Cloud</text>
              </g>
"""

CONTACT = """
              <circle class="hv-orbit" cx="230" cy="206" r="184" fill="none" stroke="url(#hvGrad)"
                stroke-opacity=".34" stroke-width="1.3" stroke-dasharray="3 12"></circle>

              <!-- brief in, reply out -->
              <path id="ctArc" class="hv-link" d="M104 300 C 150 150, 310 150, 356 300" fill="none"
                stroke="url(#hvGrad)" stroke-width="2" stroke-linecap="round"></path>
              <circle r="4.4" fill="#f6c90e">
                <animateMotion dur="3.4s" repeatCount="indefinite" rotate="auto"><mpath href="#ctArc"></mpath></animateMotion>
              </circle>
              <circle r="3.4" fill="#fff3b0" opacity=".8">
                <animateMotion dur="3.4s" begin="1.7s" repeatCount="indefinite" rotate="auto"><mpath href="#ctArc"></mpath></animateMotion>
              </circle>

              <!-- envelope -->
              <g class="hv-icon">
                <circle class="hv-halo" cx="230" cy="206" r="82" fill="#f6c90e" opacity=".14"></circle>
                <rect x="158" y="164" width="144" height="98" rx="14" fill="#1a1810" stroke="#f6c90e"
                  stroke-opacity=".5" stroke-width="1.6"></rect>
                <path d="M158 180 L230 226 L302 180" fill="none" stroke="#f6c90e" stroke-width="2.4"
                  stroke-linecap="round" stroke-linejoin="round">
                  <animate attributeName="stroke-dasharray" values="0 200;200 0" dur="3s" repeatCount="indefinite"></animate>
                </path>
              </g>

              <g class="hv-icon" style="animation-delay:1.2s">
                <circle class="hv-halo" cx="104" cy="308" r="30" fill="#ffb000" opacity=".2"></circle>
                <circle cx="104" cy="308" r="28" fill="#1a1810" stroke="#f6c90e" stroke-opacity=".45" stroke-width="1.4"></circle>
                <g transform="translate(104 308)" fill="none" stroke="#f6c90e" stroke-width="1.9"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path d="M-10 -7 H10 V5 H-2 L-7 10 V5 H-10 Z"></path>
                </g>
                <text class="hv-label" x="104" y="356">Your brief</text>
              </g>
              <g class="hv-icon" style="animation-delay:2.6s">
                <circle class="hv-halo" cx="356" cy="308" r="30" fill="#fff3b0" opacity=".16" style="animation-delay:1.5s"></circle>
                <circle cx="356" cy="308" r="28" fill="#1a1810" stroke="#f6c90e" stroke-opacity=".45" stroke-width="1.4"></circle>
                <g transform="translate(356 308)" stroke="#f6c90e" stroke-width="2.2" fill="none"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path d="M-8 0 L-2 6 L9 -6"></path>
                </g>
                <text class="hv-label" x="356" y="356">One day</text>
              </g>
"""


BLOG = """
              <circle class="hv-orbit" cx="230" cy="206" r="190" fill="none" stroke="url(#hvGrad)"
                stroke-opacity=".34" stroke-width="1.3" stroke-dasharray="3 12"></circle>

              <!-- three articles stacking up -->
              <g class="hv-icon">
                <rect x="96" y="96" width="268" height="76" rx="14" fill="#1a1810" stroke="#f6c90e"
                  stroke-opacity=".38" stroke-width="1.4"></rect>
                <rect x="116" y="116" width="36" height="36" rx="8" fill="#f6c90e" opacity=".85"></rect>
                <g stroke="#f6c90e" stroke-width="2.6" stroke-linecap="round">
                  <path d="M170 126 H320">
                    <animate attributeName="stroke-dasharray" values="0 150;150 0" dur="2.6s" repeatCount="indefinite"></animate>
                  </path>
                  <path d="M170 142 H272" stroke-opacity=".5"></path>
                </g>
              </g>

              <g class="hv-icon" style="animation-delay:1.3s">
                <rect x="96" y="192" width="268" height="76" rx="14" fill="#1a1810" stroke="#f6c90e"
                  stroke-opacity=".38" stroke-width="1.4"></rect>
                <rect x="116" y="212" width="36" height="36" rx="8" fill="#ffb000" opacity=".85"></rect>
                <g stroke="#f6c90e" stroke-width="2.6" stroke-linecap="round">
                  <path d="M170 222 H320">
                    <animate attributeName="stroke-dasharray" values="0 150;150 0" dur="2.6s" begin=".8s" repeatCount="indefinite"></animate>
                  </path>
                  <path d="M170 238 H288" stroke-opacity=".5"></path>
                </g>
              </g>

              <g class="hv-icon" style="animation-delay:2.6s">
                <rect x="96" y="288" width="268" height="76" rx="14" fill="#1a1810" stroke="#f6c90e"
                  stroke-opacity=".38" stroke-width="1.4"></rect>
                <rect x="116" y="308" width="36" height="36" rx="8" fill="#fff3b0" opacity=".8"></rect>
                <g stroke="#f6c90e" stroke-width="2.6" stroke-linecap="round">
                  <path d="M170 318 H320">
                    <animate attributeName="stroke-dasharray" values="0 150;150 0" dur="2.6s" begin="1.6s" repeatCount="indefinite"></animate>
                  </path>
                  <path d="M170 334 H256" stroke-opacity=".5"></path>
                </g>
              </g>

              <!-- pen nib marking the newest post -->
              <g class="hv-icon" style="animation-delay:.6s">
                <circle class="hv-halo" cx="366" cy="106" r="26" fill="#f6c90e" opacity=".26"></circle>
                <circle cx="366" cy="106" r="24" fill="#1a1810" stroke="#f6c90e" stroke-opacity=".5"
                  stroke-width="1.4"></circle>
                <g transform="translate(366 106)" fill="none" stroke="#f6c90e" stroke-width="2.2"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path d="M-8 8 L-8 3 L4 -9 L9 -4 L-3 8 Z"></path>
                  <path d="M2 -7 L7 -2"></path>
                </g>
              </g>
"""

VISUALS = {
    "/blog/": (BLOG, "New posts monthly"),
    "/services/": (SERVICES, "Build &middot; Publish &middot; Support"),
    "/cloud/": (CLOUD, "Configure &middot; Deploy &middot; Maintain"),
    "/support/": (SUPPORT, "Watch &middot; Fix &middot; Verify"),
    "/courses/": (COURSES, "Learn &middot; Practise &middot; Apply"),
    "/careers/": (CAREERS, "Roles open now"),
    "/contact/": (CONTACT, "Reply within one business day"),
}
