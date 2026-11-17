# Treinamento RAG: Arquitetura de Dados, Base de Conhecimento & Simulação

Este documento sintetiza o processo de **captura, limpeza, categorização** dos dados do projeto, o **contrato de dados sintéticos para telemetria de astronautas**, a **declaração ética para o pitch**, e o **roteiro de integração com os datasets do Google Drive**, utilizando o **Ollama local** (`llama3.2:3b` e `nomic-embed-text`).

---

## 📌 1. Captura, Limpeza e Categorização dos Datasets

O projeto unifica três fontes primárias de dados locais com bases públicas de apoio:

```
Treinamento-RAG/
├── 1-ia-base-conhecimento/    --> Literatura biomédica espacial, relatórios LSAH e protocolos (.md)
├── 2-DATASET-NASA/            --> Experimentos biomédicos do LSDA e NASA Open Data (.xls, .pdf, .tif)
├── 3-api/                     --> Conexões ativas com Hugging Face (Astronaut Database + Evo2 VEP)
└── schemas/                   --> Contratos de dados sintéticos (evento-atualizado.schema.json)
```

### A. Base de Conhecimento (`1-ia-base-conhecimento/`)
* **Ação de Limpeza:** Foram removidas cópias e arquivos duplicados com sufixos `* - Copia*.md` e `* (1).md` (ex.: *causal_diagramming*, *levels_of_evidence*, *the_effects_of_galactic_cosmic_rays*), consolidando a base em **30 documentos canônicos** em formato Markdown limpo.
* **Categorização dos Documentos:**
  1. **Vigilância Médica Ocupacional & LSAH:**
     * Histórico do projeto *Lifetime Surveillance of Astronaut Health* (Newsletters vols. 27 a 31 e Spring 2011).
     * Salvaguarda da saúde da comunidade de astronautas da NASA (APHA 2016).
     * Avaliação de dados de exposição ocupacional e protocolos de acompanhamento contínuo.
  2. **Radiação Cósmica Galáctica (GCR) e Riscos em Missões de Exploração:**
     * Efeitos de raios cósmicos galácticos sobre o Sistema Nervoso Central (SNC).
     * Fluxo de partículas HZE como risco em futuras missões a Marte.
     * Limitações preditivas de risco de radiação e blindagem magnética solenoidal.
  3. **Adaptação à Microgravidade, Biomarcadores & Fisiologia Aeroespacial:**
     * Efeitos da microgravidade na saúde de astronautas femininas.
     * Monitoramento de biomarcadores para atrofia muscular via chip eletrônico (HRP/IWS 2021).
     * Monitoramento nanoscópico e ressonância magnética radial ultracurta da cartilagem lombar.
     * Diretrizes da Subdivisão de Fisiologia Aeroespacial (SDFA / IMAE - FAB): câmara hipobárica, desorientação espacial e adaptação fisiológica.
  4. **Modelagem Causal de Riscos e Eventos de Saúde:**
     * Diagramação causal para avaliação de riscos do sistema humano em voo espacial.
     * Níveis de evidência científica para avaliação de risco clínico.
     * Identificação de eventos de saúde em missões espaciais (MIAS / IWS 2021).
  5. **Modelagem Computacional e Inteligência Artificial:**
     * Otimização hiperparamétrica agentic ciente da saúde do astronauta em estados quânticos de redes neurais (NQS).

---

### B. Datasets Experimentais NASA (`2-DATASET-NASA/`)
Base de dados empíricos contendo mais de 700 planilhas XLS/XLSX, relatórios técnicos em PDF e exames de imagem obtidos de missões reais e modelos análogos:
* **Neurovestibular e Síndrome de Adaptação Espacial (SMS):**
  * *Apollo Flight Crew Vestibular Assessment* (avaliações vestibulares das tripulações Apollo).
  * *Validation of Predictive Tests and Countermeasures for Space Motion Sickness*.
  * Estudos de integração otolítica e de canais semicirculares (*COIS*).
* **Neuromuscular, Biometria de Voo & Análogos de Bed Rest:**
  * Medidas padrão de repouso no leito (*Bed Rest Standard Measures - Tendon Reflex*).
  * Planilhas biométricas de voo (*FltBdyWt.XLS*, *FlDlyWtr.XLS*, *FltDlyFd.XLS*, *OrgnWt_A.XLS*, séries *COMB156* a *COMB165*): ingestão de água, consumo alimentar, massa corporal e peso de órgãos em microgravidade.
* **Oftalmologia & Síndrome Neuro-ocular (SANS):**
  * Tonometria e pressão intraocular na coorte do LSAH (*Intraocular Pressure in the LSAH Population*).
* **Ambiente de Cabine e Suporte de Vida:**
  * Medições de ruído acústico durante testes de câmara de suporte de vida (*Acoustic Noise During the Phase III Chamber Test*).

---

### C. Conexões com APIs Externas (`3-api/`)
* **Astronaut Database (`juliensimon/astronaut-database`):**
  * Metadados completos consolidados de **870 astronautas** salvos em [`3-api/astronauts_complete.json`](./3-api/astronauts_complete.json), [`3-api/astronauts.csv`](./3-api/astronauts.csv) e [`3-api/astronauts.parquet`](./3-api/astronauts.parquet).
  * Variáveis: nacionalidade, horas no espaço, número de missões, empregadores, datas vitais e Wikidata ID.
* **Genômica Espacial (`jang1563/evo2-spaceflight-vep`):**
  * Primeiras 100 variantes genômicas analisadas sob estresse de voo espacial salvas em [`3-api/evo2_first_rows.json`](./3-api/evo2_first_rows.json).
  * Predições do modelo biológico fundacional Evo2 para variantes e classificações ClinVar.

---

### D. Dados Públicos de Apoio Adicionais
1. **PhysioNet CinC 2017 Challenge:**
   * Base de sinais fisiológicos de ECG de derivação única para detecção e classificação de fibrilação atrial e arritmias cardíacas em tempo real.
2. **NASA Open Data Portal & LSDA (Life Sciences Data Archive):**
   * Repositório público oficial da NASA com mais de 500 estudos biomédicos e protocolos desidentificados.
3. **Aba Resources do Desafio:**
   * Diretrizes técnicas, requisitos de interoperabilidade e dicionários de termos.

---

## 🛡️ 2. Contrato de Dados Sintéticos e Declaração Ética para o Pitch

### O Contrato JSON: `evento-atualizado.schema.json`
Para a tarefa da **Pessoa 1**, foi estruturado e disponibilizado o contrato padrão em [`schemas/evento-atualizado.schema.json`](./schemas/evento-atualizado.schema.json) com um evento de exemplo validado em [`schemas/sample-evento-simulado.json`](./schemas/sample-evento-simulado.json):
* **Identificação:** `evento_id` (UUID), `timestamp` (ISO 8601), `astronauta_id`, `missao`.
* **Flag Obrigatória de Integridade Ética:** `"is_simulado": true`.
* **Sinais Vitais:** Frequência cardíaca (bpm), pressão arterial sistólica/diastólica, SpO2 (%), frequência respiratória (rpm), temperatura corporal (°C), variabilidade da frequência cardíaca (RMSSD ms).
* **Ambiente e Telemetria de Cabine:** Atividade (EVA, nominal, repouso), pressão de cabine (kPa), taxa de radiação ($\mu\text{Gy/h}$), radiação acumulada (mGy) e nível de microgravidade ($g$).
* **Classificação Clínica:** `VERDE_NOMINAL`, `AMARELO_ATENCAO`, `LARANJA_ALERTA`, `VERMELHO_CRITICO`.

### 🎤 Declaração Obrigatória para o Pitch
> **"Dados médicos e biomédicos reais de astronautas em missão são extremamente raros, restritos e protegidos por rigorosas leis internacionais de sigilo médico (HIPAA) e comitês de ética da NASA (Institutional Review Board - IRB).**  
> **Por essa razão, nossa solução utiliza dados biomédicos de telemetria individual 100% sintéticos e simulados com alta fidelidade matemática através do contrato `evento-atualizado.schema.json`. Paralelamente, todo o raciocínio clínico da nossa IA é sustentado por conhecimento científico real e aberto da NASA (LSDA, LSAH), PhysioNet CinC e literatura biomédica espacial."**

---

## 🔄 3. Como Juntar os Datasets Locais com os Datasets do Google Drive

Para unificar os dados já organizados localmente com os arquivos armazenados no **Google Drive**, siga os procedimentos abaixo:

### Método A: Google Drive for Desktop (Sincronização Direta - Recomendado)
1. Instale e abra o aplicativo oficial **Google Drive for Desktop** no Windows. O Drive criará uma unidade virtual (ex.: `G:\` ou `H:\`).
2. Localize a pasta dos datasets na unidade virtual (ex.: `G:\Meu Drive\NASA_DATASETS`).
3. Execute o script automatizado criado na raiz do projeto:
   ```bash
   python sync_gdrive.py --source "G:\Meu Drive\NASA_DATASETS" --target 2-DATASET-NASA
   ```
   * O script compara datas de modificação, ignora arquivos temporários e copia apenas arquivos novos ou atualizados.
   * Para simular sem copiar, utilize a flag `--dry-run`:
     ```bash
     python sync_gdrive.py --source "G:\Meu Drive\NASA_DATASETS" --target 2-DATASET-NASA --dry-run
     ```

### Método B: Script Python Automatizado via PyDrive2 / Service Account
Caso a sincronização ocorra em ambiente de servidor ou nuvem sem Google Drive for Desktop:
1. Ative a Google Drive API no Google Cloud Console e baixe o `client_secrets.json`.
2. Configure a rotina de download automatizada em lote mapeando as IDs das pastas do Drive para as pastas locais correspondentes (`1-ia-base-conhecimento/`, `2-DATASET-NASA/` ou `3-api/`).

### Método C: Unificação Vetorial no Pipeline RAG com Ollama
Uma vez que os arquivos do Google Drive forem baixados para a pasta local correspondente:
1. Reindexe a base vetorial utilizando o script [`3-api/rag_ollama.py`](./3-api/rag_ollama.py) com o modelo `nomic-embed-text:latest`.
2. O sistema atualizará os embeddings no arquivo de cache [`3-api/astronauts_embeddings.npz`](./3-api/astronauts_embeddings.npz), integrando as novas informações ao mecanismo de busca por similaridade semântica.

---

## 🤖 4. Execução com Ollama Local

Todo o processamento de busca vetorial e inferência de linguagem natural roda **localmente**:
* **Servidor Ollama:** `http://127.0.0.1:11434`
* **Modelo de Embeddings:** `nomic-embed-text:latest` (vetores de 768 dimensões)
* **Modelo LLM de Raciocínio:** `llama3.2:3b`

Para realizar consultas RAG locais na base consolidada:
```bash
python 3-api/rag_ollama.py --query "Quais os principais riscos de radiação em missões de exploração a Marte segundo o LSAH?"
```
